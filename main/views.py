from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Portfolio, ContactInfo, DeliveryInfo, PaymentInfo, TermsInfo, ContentBlock
from .forms import OrderForm
import logging

logger = logging.getLogger(__name__)

def index(request):
    services = Service.objects.all()
    portfolio = Portfolio.objects.all()
    contact = ContactInfo.objects.first()
    delivery = DeliveryInfo.objects.all()
    payment = PaymentInfo.objects.all()
    terms = TermsInfo.objects.all()
    content_blocks = ContentBlock.objects.filter(is_active=True)  # добавили
    popup_court = ContentBlock.objects.filter(block_type='popup', title__icontains='суд').first()

    success = False
    show_modal = False
    from_bottom_form = False

    if request.method == 'POST':
        form = OrderForm(request.POST)
        source = request.POST.get('form_source', '')
        if source == 'modal':
            show_modal = True
        else:
            from_bottom_form = True

        if form.is_valid():
            order = form.save()
            subject = f'Новая заявка с сайта от {order.name}'
            message = f'''
            Имя: {order.name}
            Телефон: {order.phone}
            Email: {order.email if order.email else 'не указан'}
            Комментарий: {order.comment if order.comment else 'нет'}
            '''
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['artm.vyv@mail.ru']

            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                success = True
                form = OrderForm()
            except Exception as e:
                logger.error(f'Ошибка отправки письма: {e}')
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
        'content_blocks': content_blocks,
        'popup_court': popup_court,
        'form': form,
        'success': success,
        'show_modal': show_modal,
        'from_bottom_form': from_bottom_form,
    }
    return render(request, 'main/index.html', context)