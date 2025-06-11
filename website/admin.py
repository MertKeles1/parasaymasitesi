from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import (
    SiteSettings, ProductCategory, Product, BlogCategory, BlogPost,
    Testimonial, AboutPage, CompanyValue, FAQ, ContactMessage,
    NewsletterSubscriber, HomeSlider
)

# Site Ayarları Admin
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Genel Bilgiler', {
            'fields': ('site_title', 'site_description', 'logo', 'favicon')
        }),
        ('İletişim Bilgileri', {
            'fields': ('phone_primary', 'phone_secondary', 'email_primary', 'email_secondary', 'address')
        }),
        ('Çalışma Saatleri', {
            'fields': ('working_hours_weekday', 'working_hours_saturday', 'working_hours_sunday')
        }),
        ('Sosyal Medya', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'youtube_url'),
            'classes': ('collapse',)
        }),
        ('SEO Ayarları', {
            'fields': ('meta_keywords', 'google_analytics'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Sadece bir tane SiteSettings olabilir
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False

# Ürün Kategorileri Admin
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active', 'product_count']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']
    
    def product_count(self, obj):
        count = obj.product_set.count()
        if count > 0:
            url = reverse('admin:website_product_changelist') + f'?category__id__exact={obj.id}'
            return format_html('<a href="{}">{} ürün</a>', url, count)
        return "0 ürün"
    product_count.short_description = "Ürün Sayısı"

# Ürünler Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_display', 'is_featured', 'is_active', 'in_stock', 'order']
    list_filter = ['category', 'is_featured', 'is_active', 'in_stock', 'created_at']
    search_fields = ['name', 'description', 'short_description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_featured', 'is_active', 'in_stock', 'order']
    readonly_fields = ['created_at', 'updated_at', 'image_preview']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('name', 'slug', 'category', 'short_description', 'description')
        }),
        ('Fiyat ve Özellikler', {
            'fields': ('price', 'features', 'technical_specs')
        }),
        ('Görsel', {
            'fields': ('image', 'image_preview', 'image_alt')
        }),
        ('Durum', {
            'fields': ('is_featured', 'is_active', 'in_stock', 'order')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Tarihler', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def price_display(self, obj):
        if obj.price:
            return f"₺{obj.price:,.2f}"
        return "Fiyat belirtilmemiş"
    price_display.short_description = "Fiyat"
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px; max-width: 300px;">')
        return "Resim yok"
    image_preview.short_description = "Resim Önizleme"

# Blog Kategorileri Admin
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'post_count']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active']
    
    def post_count(self, obj):
        count = obj.get_post_count()
        if count > 0:
            url = reverse('admin:website_blogpost_changelist') + f'?category__id__exact={obj.id}'
            return format_html('<a href="{}">{} yazı</a>', url, count)
        return "0 yazı"
    post_count.short_description = "Yazı Sayısı"

# Blog Yazıları Admin
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'is_published', 'is_featured', 'published_date', 'view_count']
    list_filter = ['category', 'author', 'is_published', 'is_featured', 'published_date']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published', 'is_featured']
    readonly_fields = ['created_at', 'updated_at', 'image_preview', 'view_count']
    date_hierarchy = 'published_date'
    ordering = ['-published_date']
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('title', 'slug', 'category', 'author', 'excerpt')
        }),
        ('İçerik', {
            'fields': ('content',)
        }),
        ('Görsel', {
            'fields': ('featured_image', 'image_preview', 'image_alt')
        }),
        ('Durum', {
            'fields': ('is_published', 'is_featured', 'published_date')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'keywords'),
            'classes': ('collapse',)
        }),
        ('İstatistikler ve Tarihler', {
            'fields': ('view_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.featured_image:
            return mark_safe(f'<img src="{obj.featured_image.url}" style="max-height: 200px; max-width: 300px;">')
        return "Resim yok"
    image_preview.short_description = "Resim Önizleme"

# Müşteri Yorumları Admin
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_title', 'rating', 'is_active', 'order', 'created_at']
    list_filter = ['rating', 'is_active', 'created_at']
    search_fields = ['client_name', 'client_title', 'content']
    list_editable = ['is_active', 'order']
    readonly_fields = ['created_at', 'photo_preview']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Müşteri Bilgileri', {
            'fields': ('client_name', 'client_title', 'client_photo', 'photo_preview')
        }),
        ('Yorum', {
            'fields': ('content', 'rating')
        }),
        ('Durum', {
            'fields': ('is_active', 'order', 'created_at')
        }),
    )
    
    def photo_preview(self, obj):
        if obj.client_photo:
            return mark_safe(f'<img src="{obj.client_photo.url}" style="max-height: 100px; max-width: 100px; border-radius: 50%;">')
        return "Fotoğraf yok"
    photo_preview.short_description = "Fotoğraf Önizleme"

# Hakkımızda Admin
@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Şirket Hikayesi', {
            'fields': ('story_title', 'story_content', 'story_image', 'image_preview')
        }),
        ('İstatistikler', {
            'fields': ('years_experience', 'happy_customers', 'product_varieties', 'cities_served')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['image_preview', 'updated_at']
    
    def has_add_permission(self, request):
        return not AboutPage.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def image_preview(self, obj):
        if obj.story_image:
            return mark_safe(f'<img src="{obj.story_image.url}" style="max-height: 200px; max-width: 300px;">')
        return "Resim yok"
    image_preview.short_description = "Resim Önizleme"

# Şirket Değerleri Admin
@admin.register(CompanyValue)
class CompanyValueAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_display', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['is_active', 'order']
    ordering = ['order']
    
    def icon_display(self, obj):
        return mark_safe(f'<i class="{obj.icon_class}" style="font-size: 20px;"></i>')
    icon_display.short_description = "İkon"

# SSS Admin
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question_short', 'category', 'is_active', 'order']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['question', 'answer', 'category']
    list_editable = ['is_active', 'order']
    ordering = ['order', 'question']
    
    def question_short(self, obj):
        return obj.question[:80] + "..." if len(obj.question) > 80 else obj.question
    question_short.short_description = "Soru"

# İletişim Mesajları Admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject_display', 'is_read', 'is_replied', 'created_at']
    list_filter = ['subject', 'is_read', 'is_replied', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'phone', 'subject', 'message', 'created_at']
    list_editable = ['is_read', 'is_replied']
    ordering = ['-created_at']
    
    actions = ['mark_as_read', 'mark_as_replied']
    
    def subject_display(self, obj):
        return obj.get_subject_display()
    subject_display.short_description = "Konu"
    
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} mesaj okundu olarak işaretlendi.')
    mark_as_read.short_description = "Seçilen mesajları okundu olarak işaretle"
    
    def mark_as_replied(self, request, queryset):
        updated = queryset.update(is_replied=True)
        self.message_user(request, f'{updated} mesaj cevaplandı olarak işaretlendi.')
    mark_as_replied.short_description = "Seçilen mesajları cevaplandı olarak işaretle"
    
    def has_add_permission(self, request):
        return False

# Bülten Aboneleri Admin
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'subscribed_at']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email']
    list_editable = ['is_active']
    readonly_fields = ['subscribed_at']
    ordering = ['-subscribed_at']
    
    actions = ['activate_subscribers', 'deactivate_subscribers']
    
    def activate_subscribers(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} abone aktif hale getirildi.')
    activate_subscribers.short_description = "Seçilen aboneleri aktif hale getir"
    
    def deactivate_subscribers(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} abone pasif hale getirildi.')
    deactivate_subscribers.short_description = "Seçilen aboneleri pasif hale getir"

# Ana Sayfa Slider Admin
@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order', 'image_preview_small']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle', 'description']
    list_editable = ['is_active', 'order']
    readonly_fields = ['image_preview']
    ordering = ['order']
    
    fieldsets = (
        ('İçerik', {
            'fields': ('title', 'subtitle', 'description')
        }),
        ('Görsel', {
            'fields': ('image', 'image_preview')
        }),
        ('Buton', {
            'fields': ('button_text', 'button_url')
        }),
        ('Durum', {
            'fields': ('is_active', 'order')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px; max-width: 300px;">')
        return "Resim yok"
    image_preview.short_description = "Resim Önizleme"
    
    def image_preview_small(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 80px;">')
        return "❌"
    image_preview_small.short_description = "Resim"

# Admin site başlık ve header özelleştirmeleri
admin.site.site_header = "2M İSTANBUL ELEKTRONİK Admin Paneli"
admin.site.site_title = "2M Admin"
admin.site.index_title = "Website Yönetim Paneli"
