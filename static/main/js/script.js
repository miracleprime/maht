document.addEventListener('DOMContentLoaded', function() {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav');
    const header = document.querySelector('.header');
    const links = document.querySelectorAll('a[href^="#"]');
    const forms = document.querySelectorAll('.contact-form');


    // Мобильное меню
    if (burger && nav) {
        burger.addEventListener('click', function() {
            nav.classList.toggle('nav--active');
            burger.classList.toggle('burger--active');
        });
    }

    // Закрытие меню при клике на ссылку
    nav?.addEventListener('click', function(e) {
        if (e.target.tagName === 'A' && nav.classList.contains('nav--active')) {
            nav.classList.remove('nav--active');
            burger?.classList.remove('burger--active');
        }
    });

    // Плавная прокрутка к якорям
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const headerHeight = header ? header.offsetHeight : 0;
                const targetPosition = targetElement.offsetTop - headerHeight;
                window.scrollTo({ top: targetPosition, behavior: 'smooth' });
            }
        });
    });

    // Обработка форм (отправка через AJAX)
    forms.forEach((form) => {
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(form);
        const submitButton = form.querySelector('button[type="submit"]');
        const originalText = submitButton ? submitButton.textContent : '';

        if (submitButton) {
        submitButton.textContent = 'Отправка...';
        submitButton.disabled = true;
        }

        const csrf = form.querySelector('[name=csrfmiddlewaretoken]')?.value;

        fetch(form.getAttribute('action') || '/submit-order/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            ...(csrf ? { 'X-CSRFToken': csrf } : {})
        }
        })
        .then(r => r.json())
        .then(data => {
        if (data.success) {
            showMessage('Спасибо! Мы свяжемся с вами.', 'success');
            form.reset();
        } else {
            showMessage('Ошибка: ' + (data.error || 'Проверьте поля'), 'error');
        }
        })
        .catch(() => showMessage('Ошибка соединения. Попробуйте позже.', 'error'))
        .finally(() => {
        if (submitButton) {
            submitButton.textContent = originalText;
            submitButton.disabled = false;
        }
        });
    });
    });


    function showMessage(text, type) {
        const div = document.createElement('div');
        div.textContent = text;
        div.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? '#4CAF50' : '#f44336'};
            color: white;
            padding: 15px 20px;
            border-radius: 5px;
            z-index: 9999;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        `;
        document.body.appendChild(div);
        setTimeout(() => div.remove(), 5000);
    }

    // Липкая шапка при скролле
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 100) {
                header.classList.add('header--scrolled');
            } else {
                header.classList.remove('header--scrolled');
            }
        });
    }
});