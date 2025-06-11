from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Site Ayarları
class SiteSettings(models.Model):
    site_title = models.CharField(max_length=100, default="2M ISTANBUL ELEKTRONİK")
    site_description = models.TextField(default="Para sayma makineleri ve çözümleri için güvenilir adres")
    logo = models.ImageField(upload_to='site/', null=True, blank=True)
    favicon = models.ImageField(upload_to='site/', null=True, blank=True)
    
    # İletişim Bilgileri
    phone_primary = models.CharField(max_length=20, default="+90 123 456 78 90")
    phone_secondary = models.CharField(max_length=20, blank=True)
    email_primary = models.EmailField(default="info@2mistanbul.com")
    email_secondary = models.EmailField(blank=True)
    address = models.TextField(default="Merkez Mah. Atatürk Cad. No:123 Kat:5, İstanbul")
    
    # Çalışma Saatleri
    working_hours_weekday = models.CharField(max_length=50, default="09:00 - 18:00")
    working_hours_saturday = models.CharField(max_length=50, default="09:00 - 15:00")
    working_hours_sunday = models.CharField(max_length=50, default="Kapalı")
    
    # Sosyal Medya
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    
    # SEO
    meta_keywords = models.TextField(blank=True)
    google_analytics = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Site Ayarları"
        verbose_name_plural = "Site Ayarları"
    
    def __str__(self):
        return self.site_title
    
    @property
    def phone(self):
        return self.phone_primary
    
    @property 
    def email(self):
        return self.email_primary
    
    def save(self, *args, **kwargs):
        # Sadece bir tane SiteSettings olabilir
        if not self.pk and SiteSettings.objects.exists():
            raise ValueError('Sadece bir Site Ayarları kaydı olabilir')
        super().save(*args, **kwargs)

# Ürün Kategorileri
class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori Adı")
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, verbose_name="Açıklama")
    image = models.ImageField(upload_to='categories/', blank=True, verbose_name="Kategori Resmi")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")
    
    class Meta:
        verbose_name = "Ürün Kategorisi"
        verbose_name_plural = "Ürün Kategorileri"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
    
    def get_product_count(self):
        return self.product_set.filter(is_active=True).count()

# Ürünler
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ürün Adı")
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Kategori")
    description = models.TextField(verbose_name="Açıklama")
    short_description = models.CharField(max_length=300, verbose_name="Kısa Açıklama")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Fiyat")
    
    # Ürün Özellikleri
    features = models.TextField(help_text="Her satıra bir özellik yazın", verbose_name="Özellikler")
    technical_specs = models.TextField(blank=True, verbose_name="Teknik Özellikler")
    
    # Görsel
    image = models.ImageField(upload_to='products/', verbose_name="Ana Resim")
    image_alt = models.CharField(max_length=200, blank=True, verbose_name="Resim Alt Text")
    
    # Durum
    is_featured = models.BooleanField(default=False, verbose_name="Öne Çıkan")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    in_stock = models.BooleanField(default=True, verbose_name="Stokta")
    
    # SEO
    meta_title = models.CharField(max_length=60, blank=True, verbose_name="Meta Başlık")
    meta_description = models.CharField(max_length=160, blank=True, verbose_name="Meta Açıklama")
    
    # Tarihler
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Sıralama
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")
    
    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.name
    
    def get_features_list(self):
        return [feature.strip() for feature in self.features.split('\n') if feature.strip()]

# Blog Kategorileri
class BlogCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori Adı")
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, verbose_name="Açıklama")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    
    class Meta:
        verbose_name = "Blog Kategorisi"
        verbose_name_plural = "Blog Kategorileri"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_post_count(self):
        return self.blogpost_set.filter(is_published=True).count()

# Blog Yazıları
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name="Kategori")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Yazar")
    
    # İçerik
    excerpt = models.TextField(max_length=300, verbose_name="Özet")
    content = models.TextField(verbose_name="İçerik")
    
    # Görsel
    featured_image = models.ImageField(upload_to='blog/', verbose_name="Öne Çıkan Resim")
    image_alt = models.CharField(max_length=200, blank=True, verbose_name="Resim Alt Text")
    
    # Durum
    is_published = models.BooleanField(default=False, verbose_name="Yayında")
    is_featured = models.BooleanField(default=False, verbose_name="Öne Çıkan")
    
    # SEO
    meta_title = models.CharField(max_length=60, blank=True, verbose_name="Meta Başlık")
    meta_description = models.CharField(max_length=160, blank=True, verbose_name="Meta Açıklama")
    keywords = models.CharField(max_length=200, blank=True, verbose_name="Anahtar Kelimeler")
    
    # Tarihler
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Yayın Tarihi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # İstatistikler
    view_count = models.PositiveIntegerField(default=0, verbose_name="Görüntülenme")
    
    class Meta:
        verbose_name = "Blog Yazısı"
        verbose_name_plural = "Blog Yazıları"
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title

# Müşteri Yorumları
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100, verbose_name="Müşteri Adı")
    client_title = models.CharField(max_length=100, verbose_name="Ünvan/Şirket")
    client_photo = models.ImageField(upload_to='testimonials/', blank=True, verbose_name="Müşteri Fotoğrafı")
    content = models.TextField(verbose_name="Yorum İçeriği")
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=5, verbose_name="Puan")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Müşteri Yorumu"
        verbose_name_plural = "Müşteri Yorumları"
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f"{self.client_name} - {self.client_title}"

# Hakkımızda Sayfası
class AboutPage(models.Model):
    # Şirket Hikayesi
    story_title = models.CharField(max_length=200, default="Hikayemiz", verbose_name="Hikaye Başlığı")
    story_content = models.TextField(verbose_name="Hikaye İçeriği")
    story_image = models.ImageField(upload_to='about/', blank=True, verbose_name="Hikaye Resmi")
    
    # İstatistikler
    years_experience = models.PositiveIntegerField(default=20, verbose_name="Yıllık Deneyim")
    happy_customers = models.PositiveIntegerField(default=5000, verbose_name="Mutlu Müşteri")
    product_varieties = models.PositiveIntegerField(default=30, verbose_name="Ürün Çeşidi")
    cities_served = models.PositiveIntegerField(default=81, verbose_name="Hizmet Verilen İl")
    
    # SEO
    meta_title = models.CharField(max_length=60, blank=True, verbose_name="Meta Başlık")
    meta_description = models.CharField(max_length=160, blank=True, verbose_name="Meta Açıklama")
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Hakkımızda Sayfası"
        verbose_name_plural = "Hakkımızda Sayfası"
    
    def __str__(self):
        return "Hakkımızda Sayfası"
    
    def save(self, *args, **kwargs):
        if not self.pk and AboutPage.objects.exists():
            raise ValueError('Sadece bir Hakkımızda sayfası olabilir')
        super().save(*args, **kwargs)

# Şirket Değerleri
class CompanyValue(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama")
    icon_class = models.CharField(max_length=50, help_text="Font Awesome icon class (örn: fas fa-medal)", verbose_name="İkon")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")
    
    class Meta:
        verbose_name = "Şirket Değeri"
        verbose_name_plural = "Şirket Değerleri"
        ordering = ['order']
    
    def __str__(self):
        return self.title

# SSS (Sık Sorulan Sorular)
class FAQ(models.Model):
    question = models.CharField(max_length=300, verbose_name="Soru")
    answer = models.TextField(verbose_name="Cevap")
    category = models.CharField(max_length=100, blank=True, verbose_name="Kategori")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Sık Sorulan Soru"
        verbose_name_plural = "Sık Sorulan Sorular"
        ordering = ['order', 'question']
    
    def __str__(self):
        return self.question[:100]

# İletişim Formları
class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('info', 'Ürün Bilgisi'),
        ('quote', 'Fiyat Teklifi'),
        ('support', 'Teknik Destek'),
        ('complaint', 'Şikayet'),
        ('other', 'Diğer'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Ad Soyad")
    email = models.EmailField(verbose_name="E-posta")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, verbose_name="Konu")
    message = models.TextField(verbose_name="Mesaj")
    is_read = models.BooleanField(default=False, verbose_name="Okundu")
    is_replied = models.BooleanField(default=False, verbose_name="Cevaplandı")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Gönderim Tarihi")
    
    class Meta:
        verbose_name = "İletişim Mesajı"
        verbose_name_plural = "İletişim Mesajları"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.get_subject_display()}"

# Bülten Aboneleri
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="E-posta")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Abone Tarihi")
    
    class Meta:
        verbose_name = "Bülten Abonesi"
        verbose_name_plural = "Bülten Aboneleri"
        ordering = ['-subscribed_at']
    
    def __str__(self):
        return self.email

# Ana Sayfa Slider
class HomeSlider(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    subtitle = models.CharField(max_length=300, blank=True, verbose_name="Alt Başlık")
    description = models.TextField(blank=True, verbose_name="Açıklama")
    image = models.ImageField(upload_to='slider/', verbose_name="Resim")
    button_text = models.CharField(max_length=50, blank=True, verbose_name="Buton Yazısı")
    button_url = models.CharField(max_length=200, blank=True, verbose_name="Buton Linki")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")
    
    class Meta:
        verbose_name = "Ana Sayfa Slider"
        verbose_name_plural = "Ana Sayfa Slider"
        ordering = ['order']
    
    def __str__(self):
        return self.title
