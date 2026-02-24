from django.db import models

# Услуги
class Service(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    price = models.CharField('Цена', max_length=100, blank=True)
    image = models.ImageField('Изображение', upload_to='services/', blank=True, null=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

# Портфолио (примеры работ)
class Portfolio(models.Model):
    title = models.CharField('Название', max_length=200)
    category = models.CharField('Категория', max_length=100)  # например, "Визитки", "Брошюры"
    image = models.ImageField('Фото работы', upload_to='portfolio/')
    description = models.TextField('Описание', blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

# Контактные данные (телефон, email, адрес)
class ContactInfo(models.Model):
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')
    address = models.CharField('Адрес', max_length=300)
    work_hours = models.CharField('Режим работы', max_length=200, blank=True)
    map_link = models.URLField('Ссылка на карту', blank=True)  # iframe с Яндекс/Google картой

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'

    def __str__(self):
        return f'Контакты: {self.phone}'

# Заявки с формы
class Order(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email', blank=True, null=True)
    comment = models.TextField('Комментарий', blank=True)
    created_at = models.DateTimeField('Дата заявки', auto_now_add=True)
    is_processed = models.BooleanField('Обработано', default=False)

    def __str__(self):
        return f'{self.name} - {self.phone}'

class DeliveryInfo(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='delivery/', blank=True, null=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'
        ordering = ['order']

    def __str__(self):
        return self.title

class PaymentInfo(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='payment/', blank=True, null=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'
        ordering = ['order']

    def __str__(self):
        return self.title

class TermsInfo(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='terms/', blank=True, null=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Сроки'
        verbose_name_plural = 'Сроки'
        ordering = ['order']

    def __str__(self):
        return self.title