from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import (
    Service, Portfolio, ContactInfo, DeliveryInfo,
    PaymentInfo, TermsInfo, ContentBlock, SiteSettings
)
from .forms import OrderForm


def index(request):
    services = Service.objects.all()
    portfolio = Portfolio.objects.all()
    contact = ContactInfo.objects.first()
    delivery = DeliveryInfo.objects.all()
    payment = PaymentInfo.objects.all()
    terms = TermsInfo.objects.all()
    content_blocks = ContentBlock.objects.filter(is_active=True)
    sitesettings = SiteSettings.objects.first()
    form = OrderForm()

    return render(request, 'main/index.html', {
        'services': services,
        'portfolio': portfolio,
        'contact': contact,
        'delivery': delivery,
        'payment': payment,
        'terms': terms,
        'content_blocks': content_blocks,
        'contentblocks': content_blocks,
        'sitesettings': sitesettings,
        'site_settings': sitesettings,
        'form': form,
    })

@require_POST
def submit_order(request):
    form = OrderForm(request.POST)

    if not form.is_valid():
        return JsonResponse({
            'success': False,
            'error': 'Проверьте поля формы',
            'form_errors': form.errors,
        }, status=400)

    order = form.save()

    subject = f'Новая заявка от {order.name}'
    message_lines = [
        f'Имя: {order.name}',
        f'Телефон: {order.phone}',
    ]

    if order.email:
        message_lines.append(f'Email: {order.email}')
    if order.comment:
        message_lines.append(f'Комментарий: {order.comment}')

    try:
        send_mail(
            subject,
            "\n".join(message_lines),
            settings.DEFAULT_FROM_EMAIL,
            ['artm.vyv@mail.ru'],
            fail_silently=False
        )
    except Exception:
        return JsonResponse({'success': True, 'mail_sent': False})

    return JsonResponse({'success': True, 'mail_sent': True})
