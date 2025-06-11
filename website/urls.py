from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('urunler/', views.urunler, name='urunler'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('blog/', views.blog, name='blog'),
    
    # Detay sayfaları
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('urun/<slug:slug>/', views.product_detail, name='product_detail'),
    
    # AJAX endpoints
    path('api/newsletter-subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
] 