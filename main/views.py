from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Portfolio, ContactInfo, DeliveryInfo, PaymentInfo, TermsInfo
from .forms import OrderForm
import logging

logger = logging.getLogger(__name__)

def index(request):
    services = Service.objects.all()
    portfolio = Portfolio.objects.all()
    contact = ContactInfo.objects.first()
    delivery = DeliveryInfo.objects.all()   # если несколько записей
    payment = PaymentInfo.objects.all()
    terms = TermsInfo.objects.all()
    success = False

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Сохраняем заявку в базу
            order = form.save()

            # Формируем письмо
            subject = f'Новая заявка с сайта от {order.name}'
            message = f'''
            Имя: {order.name}
            Телефон: {order.phone}
            Email: {order.email if order.email else 'не указан'}
            Комментарий: {order.comment if order.comment else 'нет'}
            '''
            # От кого — берём из настроек, но можно и явно указать
            from_email = settings.DEFAULT_FROM_EMAIL  # или settings.EMAIL_HOST_USER
            # Кому — ЗДЕСЬ ВСТАВЬ РЕАЛЬНЫЙ EMAIL МЕНЕДЖЕРОВ!
            recipient_list = ['manager@your-typography.ru']

            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                success = True
                form = OrderForm()  # очищаем форму
            except Exception as e:
                # Если письмо не отправилось, но заявка сохранилась — логируем ошибку
                logger.error(f'Ошибка отправки письма: {e}')
                # Всё равно показываем успех, чтобы клиент не паниковал
                success = True
                form = OrderForm()
    else:
        form = OrderForm()

    context = {
        'services': services,
        'portfolio': portfolio,
        'contact': contact,
        'delivery': delivery,
        'payment': payment,
        'terms': terms,
        'form': form,
        'success': success,
    }
    return render(request, 'main/index.html', context)