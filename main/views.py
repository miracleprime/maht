from django.shortcuts import render
from .models import Service, Portfolio, ContactInfo
from .forms import OrderForm  # Добавь импорт формы

def index(request):
    services = Service.objects.all()
    portfolio = Portfolio.objects.all()
    contact = ContactInfo.objects.first()
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # Можно добавить уведомление в Telegram
            success = True
            form = OrderForm()  # Очищаем форму после отправки
    else:
        form = OrderForm()
        success = False
    
    context = {
        'services': services,
        'portfolio': portfolio,
        'contact': contact,
        'form': form,
        'success': success,
    }
    return render(request, 'main/index.html', context)