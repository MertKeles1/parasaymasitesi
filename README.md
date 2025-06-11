# Django Web Sitesi Projesi

Bu klasörde Django web framework'ü kuruldu ve tam özellikli bir web sitesi için gerekli paketler eklendi.

## Kurulum

1. Virtual environment'ı aktifleştir:
```bash
source venv_new/bin/activate
```

2. Tüm bağımlılıkları kur:
```bash
pip install -r requirements.txt
```

## Kullanım

1. Geliştirme sunucusunu başlat:
```bash
python manage.py runserver
```

2. Tarayıcıda şu adrese git: http://127.0.0.1:8000/

## Web Sitesi Özellikleri

Requirements.txt dosyasında aşağıdaki özellikler için paketler bulunmaktadır:

### 🔐 Kimlik Doğrulama ve Güvenlik
- **django-allauth**: Sosyal medya girişi (Google, Facebook, GitHub vb.)
- **djangorestframework-simplejwt**: JWT token tabanlı API kimlik doğrulama

### 🎨 Kullanıcı Arayüzü
- **django-crispy-forms** + **crispy-bootstrap5**: Güzel form tasarımları
- **django-bootstrap5**: Bootstrap 5 entegrasyonu
- **django-widget-tweaks**: Form widget özelleştirme

### 📷 Medya ve Dosya Yönetimi
- **Pillow**: Resim işleme ve yeniden boyutlandırma
- **django-storages**: Cloud storage (AWS S3 vb.) desteği

### 🚀 API Geliştirme
- **djangorestframework**: RESTful API oluşturma
- **django-cors-headers**: Cross-Origin Resource Sharing
- **django-filter**: API filtreleme

### ⚡ Performans ve Geliştirme
- **django-debug-toolbar**: Geliştirme aracı
- **django-extensions**: Ek Django komutları
- **django-compressor**: CSS/JS sıkıştırma

### 📊 İçerik Yönetimi
- **django-admin-interface**: Gelişmiş admin paneli
- **django-import-export**: Veri içe/dışa aktarma
- **django-mptt**: Ağaç yapısında veriler
- **django-taggit**: Etiketleme sistemi

### 📧 E-posta ve Arka Plan İşleri
- **celery**: Arka plan görevleri
- **redis**: Message broker

### 🔍 SEO ve Meta
- **django-meta**: Meta tag yönetimi

### 🚀 Production
- **gunicorn**: WSGI server
- **whitenoise**: Statik dosya sunumu

## Proje Yapısı

- `myproject/` - Django proje ayarları
- `manage.py` - Django yönetim komutları için araç
- `venv/` - Python virtual environment
- `requirements.txt` - Tüm bağımlılık listesi

## Yararlı Komutlar

- Yeni uygulama oluştur: `python manage.py startapp appname`
- Süper kullanıcı oluştur: `python manage.py createsuperuser`
- Migration oluştur: `python manage.py makemigrations`
- Migration'ları uygula: `python manage.py migrate`
- Statik dosyaları topla: `python manage.py collectstatic`

## Gelişmiş Özellikler

1. **API Endpoints**: `/api/` URL'lerinde RESTful API
2. **Admin Panel**: `/admin/` gelişmiş yönetim paneli
3. **Kullanıcı Kayıt/Giriş**: Sosyal medya entegrasyonu
4. **Dosya Yükleme**: Resim ve dosya yönetimi
5. **Etiketleme**: İçerik etiketleme sistemi
6. **Tree Structure**: Hiyerarşik veri yapıları

## Sonraki Adımlar

1. Paketleri kullanmak için `settings.py`'a ekleyin
2. URL konfigürasyonlarını yapın
3. Template'ler ve static dosyalar oluşturun
4. API endpoint'leri tanımlayın
5. Celery konfigürasyonu yapın (opsiyonel) 
