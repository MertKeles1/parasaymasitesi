# Django Web Sitesi Projesi

Modern ve profesyonel bir Django web sitesi projesi. İşletme web siteleri için tasarlanmış, tam özellikli ve responsive bir platform.

## 🌟 Özellikler

- **Modern Tasarım**: Responsive ve kullanıcı dostu arayüz
- **Çoklu Sayfa Yapısı**: Ana sayfa, Ürünler, Hakkımızda, Blog, İletişim
- **SEO Optimize**: Arama motoru dostu yapı
- **Admin Paneli**: Django admin ile kolay içerik yönetimi
- **API Desteği**: RESTful API endpoints
- **Medya Yönetimi**: Resim ve dosya yükleme sistemi

## 🚀 Canlı Demo

Website şu anda geliştirme aşamasında. Yerel sunucuda çalıştırarak test edebilirsiniz.

## 📋 Gereksinimler

- Python 3.8+
- Django 5.2.1
- Virtual Environment
- SQLite (geliştirme için) / PostgreSQL (production için)

## 🛠️ Kurulum

1. **Projeyi klonlayın:**
```bash
git clone https://github.com/USERNAME/REPOSITORY-NAME.git
cd 2MPROJE
```

2. **Virtual environment oluşturun ve aktifleştirin:**
```bash
python -m venv venv_new
source venv_new/bin/activate  # Linux/Mac
# veya
venv_new\Scripts\activate     # Windows
```

3. **Gerekli paketleri kurun:**
```bash
pip install -r requirements.txt
```

4. **Veritabanı migration'larını çalıştırın:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Süper kullanıcı oluşturun:**
```bash
python manage.py createsuperuser
```

6. **Statik dosyaları toplayın:**
```bash
python manage.py collectstatic
```

7. **Geliştirme sunucusunu başlatın:**
```bash
python manage.py runserver
```

8. **Tarayıcıda açın:** http://127.0.0.1:8000/

## 📁 Proje Yapısı

```
2MPROJE/
├── myproject/              # Ana proje ayarları
│   ├── settings.py         # Django ayarları
│   ├── urls.py            # Ana URL konfigürasyonu
│   └── wsgi.py            # WSGI konfigürasyonu
├── website/               # Ana uygulama
│   ├── models.py          # Veri modelleri
│   ├── views.py           # View fonksiyonları
│   ├── urls.py            # URL routing
│   └── admin.py           # Admin konfigürasyonu
├── templates/             # HTML şablonları
│   ├── base.html          # Ana şablon
│   ├── anasayfa.html      # Ana sayfa
│   ├── urunler.html       # Ürünler sayfası
│   ├── hakkimizda.html    # Hakkımızda sayfası
│   ├── blog.html          # Blog sayfası
│   └── iletisim.html      # İletişim sayfası
├── static/               # Statik dosyalar
│   ├── css/              # CSS dosyaları
│   ├── js/               # JavaScript dosyaları
│   └── images/           # Resim dosyaları
├── media/                # Kullanıcı yüklediği dosyalar
├── requirements.txt      # Python bağımlılıkları
└── manage.py            # Django yönetim komutu
```

## 🎨 Tasarım ve Renkler

- **Ana Renk Paleti:**
  - Koyu Yeşil: `#0A2815`
  - Altın: `#D4AF37`
  - Açık Mavi: `#F0FFFF` (Arka plan)
  - Beyaz: `#FFFFFF`

- **Tipografi:** Modern sans-serif fontlar
- **Responsive:** Bootstrap 5 tabanlı responsive tasarım

## 🔧 Kullanılan Teknolojiler

### Backend
- **Django 5.2.1** - Web framework
- **Django REST Framework** - API geliştirme
- **Pillow** - Resim işleme
- **SQLite** - Veritabanı (geliştirme)

### Frontend
- **HTML5** - Markup
- **CSS3** - Stil
- **Bootstrap 5** - CSS framework
- **JavaScript** - İnteraktivite
- **jQuery** - DOM manipülasyonu

### Güvenlik ve Performans
- **django-allauth** - Kimlik doğrulama
- **django-cors-headers** - CORS desteği
- **django-compressor** - CSS/JS sıkıştırma
- **whitenoise** - Statik dosya sunumu

## 📱 Sayfalar

1. **Ana Sayfa** (`/`) - Hero slider, özellikler, referanslar
2. **Ürünler** (`/urunler/`) - Ürün kataloğu ve filtreler
3. **Hakkımızda** (`/hakkimizda/`) - Şirket bilgileri ve istatistikler
4. **Blog** (`/blog/`) - Blog yazıları ve pagination
5. **İletişim** (`/iletisim/`) - İletişim formu ve harita

## 🔑 Admin Paneli

Admin paneline erişim: http://127.0.0.1:8000/admin/

Süper kullanıcı oluşturduktan sonra:
- İçerik yönetimi
- Kullanıcı yönetimi
- Medya dosya yönetimi
- Site ayarları

## 🌐 API Endpoints

- `/api/` - Ana API endpoint
- API dokümantasyonu geliştirme aşamasında

## 📞 İletişim ve Destek

Proje ile ilgili sorularınız için:
- GitHub Issues bölümünü kullanın
- Pull request'lerinizi memnuniyetle karşılarız

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🤝 Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📝 Changelog

### v1.0.0 (2024)
- İlk sürüm
- Temel sayfa yapıları
- Responsive tasarım
- Admin paneli entegrasyonu

---

⭐ Bu projeyi beğendiyseniz star vermeyi unutmayın! 