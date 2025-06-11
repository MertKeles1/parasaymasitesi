/**
 * Main JavaScript for Para Sayma Makineleri Website - Cleaned
 */

document.addEventListener('DOMContentLoaded', function() {
    // Aktif Sayfa Vurgusu
    highlightActivePage();
    
    // Mobil Menü Toggle
    setupMobileMenu();
    
    // Hero Slider (Ana sayfa için)
    if (document.querySelector('.hero-slider')) {
        setupHeroSlider();
    }
    
    // İletişim Formu Doğrulama
    if (document.querySelector('.contact-form')) {
      setupContactForm();
    }
  });
  
  /**
   * Mevcut sayfayı vurgular
   */
  function highlightActivePage() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-menu a');
    
    navLinks.forEach(link => {
      const linkPath = link.getAttribute('href');
      
      if (currentPath.includes(linkPath) && linkPath !== '/') {
        link.classList.add('active');
      } else if (currentPath === '/' && linkPath === '/') {
        link.classList.add('active');
      }
    });
  }
  
  /**
   * Mobil menü açma/kapama işlemi
   */
  function setupMobileMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (menuToggle && navMenu) {
      menuToggle.addEventListener('click', function() {
        navMenu.classList.toggle('show');
        menuToggle.classList.toggle('active');
      });
    }
  }
  
  /**
 * Hero Slider Fonksiyonu
   */
function setupHeroSlider() {
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    if (slides.length <= 1) return;
    
    let currentSlide = 0;
    
    // Slide değiştirme fonksiyonu
    function showSlide(index) {
        slides.forEach(slide => slide.classList.remove('active'));
        dots.forEach(dot => dot.classList.remove('active'));
        
        slides[index].classList.add('active');
        if (dots[index]) dots[index].classList.add('active');
    }
    
    // Sonraki slide
    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }
    
    // Önceki slide
    function prevSlide() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(currentSlide);
    }
    
    // Event listeners
    if (nextBtn) {
        nextBtn.addEventListener('click', nextSlide);
    }
    
    if (prevBtn) {
        prevBtn.addEventListener('click', prevSlide);
    }
    
    // Dot navigation
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            currentSlide = index;
            showSlide(currentSlide);
      });
    });
    
    // Otomatik slider (5 saniyede bir)
    setInterval(nextSlide, 5000);
  }
  
  /**
   * İletişim formu doğrulama
   */
  function setupContactForm() {
    const contactForm = document.querySelector('.contact-form');
    
    contactForm.addEventListener('submit', function(e) {
      let valid = true;
      
      // İsim kontrolü
      const nameInput = document.getElementById('name');
        if (nameInput && !nameInput.value.trim()) {
        valid = false;
        showError(nameInput, 'İsim alanı zorunludur');
        } else if (nameInput) {
        removeError(nameInput);
      }
      
      // E-posta kontrolü
      const emailInput = document.getElementById('email');
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      
        if (emailInput && !emailRegex.test(emailInput.value.trim())) {
        valid = false;
        showError(emailInput, 'Geçerli bir e-posta adresi giriniz');
        } else if (emailInput) {
        removeError(emailInput);
      }
      
      // Mesaj kontrolü
      const messageInput = document.getElementById('message');
        if (messageInput && !messageInput.value.trim()) {
        valid = false;
        showError(messageInput, 'Mesaj alanı zorunludur');
        } else if (messageInput) {
        removeError(messageInput);
      }
      
      // Form geçerli değilse gönderimi engelle
      if (!valid) {
        e.preventDefault();
      }
    });
    
    // Hata mesajı gösterme
    function showError(input, message) {
      const formGroup = input.closest('.form-group');
      const errorElement = formGroup.querySelector('.error-message') || document.createElement('div');
      
      errorElement.className = 'error-message';
        errorElement.style.cssText = 'color: #dc3545; font-size: 12px; margin-top: 5px;';
      errorElement.textContent = message;
      
      if (!formGroup.querySelector('.error-message')) {
        formGroup.appendChild(errorElement);
      }
      
        input.style.borderColor = '#dc3545';
    }
    
    // Hata mesajını kaldırma
    function removeError(input) {
      const formGroup = input.closest('.form-group');
      const errorElement = formGroup.querySelector('.error-message');
      
      if (errorElement) {
        formGroup.removeChild(errorElement);
      }
      
        input.style.borderColor = '#ddd';
    }
  }