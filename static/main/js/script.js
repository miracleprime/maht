document.addEventListener('DOMContentLoaded', function () {
    const header = document.getElementById('siteHeader');
    const hero = document.getElementById('top');
    const links = document.querySelectorAll('a[href^="#"]');
    const forms = document.querySelectorAll('.contact-form');

    if (!header || !hero) {
        return;
    }

    function toggleHeader() {
        const heroBottom = hero.getBoundingClientRect().bottom;

        // когда герой полностью ушёл вверх — показываем шапку
        if (heroBottom <= 0) {
            header.classList.add('is-visible');
        } else {
            header.classList.remove('is-visible');
        }
    }

    // плавная прокрутка с учётом высоты шапки
    links.forEach(link => {
        link.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (!targetId || targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (!targetElement) return;

            e.preventDefault();

            const headerOffset = header.classList.contains('is-visible')
                ? header.offsetHeight
                : 0;

            const targetPosition =
                targetElement.getBoundingClientRect().top +
                window.pageYOffset -
                headerOffset;

            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        });
    });

    // отправка форм через AJAX (по красоте, как у тебя было)
    forms.forEach(form => {
        form.addEventListener('submit', function (e) {
            e.preventDefault();

            const formData = new FormData(form);
            const submitButton = form.querySelector('button[type="submit"]');
            const originalText = submitButton ? submitButton.textContent : '';
            const csrf = form.querySelector('[name=csrfmiddlewaretoken]')?.value;

            if (submitButton) {
                submitButton.textContent = 'Отправка...';
                submitButton.disabled = true;
            }

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
                        showMessage(
                            'Ошибка: ' + (data.error || 'Проверьте поля'),
                            'error'
                        );
                    }
                })
                .catch(() =>
                    showMessage(
                        'Ошибка соединения. Попробуйте позже.',
                        'error'
                    )
                )
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

    toggleHeader();
    window.addEventListener('scroll', toggleHeader, { passive: true });
    window.addEventListener('resize', toggleHeader);
});
