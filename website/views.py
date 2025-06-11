from django.shortcuts import render, get_object_or_404
from .models import (
    SiteSettings, Product, ProductCategory, BlogPost, BlogCategory,
    Testimonial, AboutPage, CompanyValue, ContactMessage, 
    NewsletterSubscriber, HomeSlider
)
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json

def get_site_context():
    """Her sayfada kullanılacak genel site verilerini döndürür"""
    try:
        site_settings = SiteSettings.objects.first()
    except SiteSettings.DoesNotExist:
        site_settings = None
    
    return {
        'site_settings': site_settings,
        'product_categories': ProductCategory.objects.filter(is_active=True).order_by('order'),
    }

def anasayfa(request):
    context = get_site_context()
    context.update({
        'featured_products': Product.objects.filter(is_featured=True, is_active=True).order_by('order')[:4],
        'testimonials': Testimonial.objects.filter(is_active=True).order_by('order')[:3],
        'home_sliders': HomeSlider.objects.filter(is_active=True).order_by('order')[:5],
    })
    
    # Site ayarlarından istatistikleri al, yoksa varsayılan değerleri kullan
    about_page = AboutPage.objects.first()
    if about_page:
        context.update({
            'stats': {
                'years_experience': about_page.years_experience,
                'happy_customers': about_page.happy_customers,
                'product_varieties': about_page.product_varieties,
                'cities_served': about_page.cities_served,
            }
        })
    else:
        context.update({
            'stats': {
                'years_experience': 20,
                'happy_customers': 5000,
                'product_varieties': 30,
                'cities_served': 81,
            }
        })
    
    return render(request, 'anasayfa.html', context)

def urunler(request):
    context = get_site_context()
    
    # Kategori filtresi
    category_slug = request.GET.get('category')
    if category_slug:
        products = Product.objects.filter(
            category__slug=category_slug, 
            is_active=True
        ).order_by('order', 'name')
        selected_category = get_object_or_404(ProductCategory, slug=category_slug)
    else:
        products = Product.objects.filter(is_active=True).order_by('order', 'name')
        selected_category = None
    
    context.update({
        'products': products,
        'selected_category': selected_category,
        'categories': ProductCategory.objects.filter(is_active=True).order_by('order'),
    })
    
    return render(request, 'urunler.html', context)

def hakkimizda(request):
    context = get_site_context()
    
    about_page = AboutPage.objects.first()
    company_values = CompanyValue.objects.filter(is_active=True).order_by('order')
    
    context.update({
        'about_page': about_page,
        'company_values': company_values,
    })
    
    return render(request, 'hakkimizda.html', context)

def blog(request):
    context = get_site_context()
    
    # Kategori filtresi
    category_slug = request.GET.get('category')
    selected_category = None
    
    if category_slug:
        # Kategori seçilmişse, o kategorideki yazıları getir
        try:
            selected_category = BlogCategory.objects.get(slug=category_slug, is_active=True)
            blog_posts = BlogPost.objects.filter(
                category=selected_category,
                is_published=True
            ).order_by('-published_date')
        except BlogCategory.DoesNotExist:
            blog_posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')
    else:
        # Kategori seçilmemişse, tüm yazıları getir
        blog_posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')
    
    # Sayfalama - Her sayfada 5 yazı
    paginator = Paginator(blog_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Blog kategorileri
    blog_categories = BlogCategory.objects.filter(is_active=True).order_by('name')
    
    context.update({
        'page_obj': page_obj,
        'blog_categories': blog_categories,
        'selected_category': selected_category,
    })
    
    return render(request, 'blog.html', context)

def iletisim(request):
    context = get_site_context()
    
    if request.method == 'POST':
        # İletişim formu işlemi
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            # Veritabanına kaydet
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            messages.success(request, 'Mesajınız başarıyla gönderildi. En kısa sürede size dönüş yapacağız.')
        else:
            messages.error(request, 'Lütfen tüm zorunlu alanları doldurun.')
    
    return render(request, 'iletisim.html', context)

@require_POST
def newsletter_subscribe(request):
    """Bülten aboneliği için AJAX endpoint"""
    try:
        data = json.loads(request.body)
        email = data.get('email')
        
        if email:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(
                email=email,
                defaults={'is_active': True}
            )
            
            if created:
                return JsonResponse({
                    'success': True, 
                    'message': 'Bültenimize başarıyla abone oldunuz!'
                })
            else:
                return JsonResponse({
                    'success': False, 
                    'message': 'Bu e-posta adresi zaten kayıtlı.'
                })
        else:
            return JsonResponse({
                'success': False, 
                'message': 'Geçerli bir e-posta adresi girin.'
            })
    except:
        return JsonResponse({
            'success': False, 
            'message': 'Bir hata oluştu. Lütfen tekrar deneyin.'
        })

def blog_detail(request, slug):
    """Blog yazısı detay sayfası"""
    context = get_site_context()
    
    blog_post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    
    # Görüntülenme sayısını artır
    blog_post.view_count += 1
    blog_post.save(update_fields=['view_count'])
    
    # İlgili yazılar (aynı kategoriden)
    related_posts = BlogPost.objects.filter(
        category=blog_post.category,
        is_published=True
    ).exclude(id=blog_post.id).order_by('-published_date')[:3]
    
    context.update({
        'blog_post': blog_post,
        'related_posts': related_posts,
    })
    
    return render(request, 'blog_detail.html', context)

def product_detail(request, slug):
    """Ürün detay sayfası"""
    context = get_site_context()
    
    product = get_object_or_404(Product, slug=slug, is_active=True)
    
    # İlgili ürünler (aynı kategoriden)
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id).order_by('order')[:4]
    
    context.update({
        'product': product,
        'related_products': related_products,
    })
    
    return render(request, 'product_detail.html', context)
