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

class ContentBlock(models.Model):
    BLOCK_TYPES = [
        ('hero', 'Главный экран'),
        ('about', 'О компании'),
        ('advantages', 'Преимущества'),
        ('quote', 'Цитата'),
        ('text', 'Текст с изображением'),
        ('custom', 'Произвольный'),
    ]

    title = models.CharField('Заголовок', max_length=200, blank=True)
    subtitle = models.CharField('Подзаголовок', max_length=200, blank=True)
    content = models.TextField('Текст', blank=True)
    image = models.ImageField('Изображение', upload_to='blocks/', blank=True, null=True)
    image_alt = models.CharField('Альт. текст', max_length=200, blank=True)
    block_type = models.CharField('Тип блока', max_length=20, choices=BLOCK_TYPES, default='custom')
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Контентный блок'
        verbose_name_plural = 'Контентные блоки'

    def __str__(self):
        return self.title or f'Блок {self.block_type} #{self.order}'
    
class HomeSection(models.Model):
    SECTION_TYPES = [
        ('hero', 'Главный экран'),
        ('services', 'Услуги'),
        ('cards', 'Карточки'),
        ('gallery', 'Галерея'),
        ('delivery', 'Доставка'),
        ('contact', 'Контакты'),
        ('text', 'Текстовый блок'),
        ('custom', 'Произвольный блок'),
    ]

    slug = models.SlugField(
        'Код секции',
        max_length=50,
        unique=True,
        help_text='Уникальный код, например: hero, terms, payment, delivery, contact'
    )
    section_type = models.CharField('Тип секции', max_length=20, choices=SECTION_TYPES, default='text')
    menu_title = models.CharField('Название в меню', max_length=100, blank=True)
    title = models.CharField('Заголовок', max_length=200, blank=True)
    subtitle = models.CharField('Подзаголовок', max_length=255, blank=True)
    content = models.TextField('Текст', blank=True)
    image = models.ImageField('Изображение', upload_to='sections/', blank=True, null=True)
    image_alt = models.CharField('Alt текст изображения', max_length=200, blank=True)
    button_text = models.CharField('Текст кнопки', max_length=100, blank=True)
    button_url = models.CharField('Ссылка кнопки', max_length=255, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)
    show_in_menu = models.BooleanField('Показывать в меню', default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Секция главной страницы'
        verbose_name_plural = 'Секции главной страницы'

    def __str__(self):
        return self.title or self.slug


class HomeSectionItem(models.Model):
    ITEM_TYPES = [
        ('card', 'Карточка'),
        ('text', 'Текст'),
        ('image', 'Изображение'),
        ('action', 'Кнопка / ссылка'),
    ]

    section = models.ForeignKey(
        HomeSection,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Секция'
    )
    item_type = models.CharField('Тип элемента', max_length=20, choices=ITEM_TYPES, default='card')
    title = models.CharField('Заголовок', max_length=200, blank=True)
    subtitle = models.CharField('Подзаголовок', max_length=255, blank=True)
    content = models.TextField('Текст', blank=True)
    image = models.ImageField('Изображение', upload_to='section_items/', blank=True, null=True)
    image_alt = models.CharField('Alt текст изображения', max_length=200, blank=True)
    price = models.CharField('Цена / подпись', max_length=100, blank=True)
    link_text = models.CharField('Текст ссылки', max_length=100, blank=True)
    link_url = models.CharField('Ссылка', max_length=255, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Элемент секции'
        verbose_name_plural = 'Элементы секций'

    def __str__(self):
        return self.title or f'Элемент #{self.pk}'

class SiteSettings(models.Model):
    site_name = models.CharField(
        'Название сайта',
        max_length=200,
        blank=True,
        default='Типография'
    )

    hero_badge = models.CharField(
        'Текст бейджа в hero',
        max_length=255,
        blank=True,
        default='Печать для бизнеса и частных клиентов'
    )
    hero_primary_button = models.CharField(
        'Текст главной кнопки',
        max_length=100,
        blank=True,
        default='Рассчитать стоимость'
    )
    hero_secondary_button = models.CharField(
        'Текст второй кнопки',
        max_length=100,
        blank=True,
        default='Смотреть продукцию'
    )

    services_menu_title = models.CharField(
        'Название "Услуги" в меню',
        max_length=100,
        blank=True,
        default='Услуги'
    )
    services_section_title = models.CharField(
        'Заголовок раздела "Услуги"',
        max_length=200,
        blank=True,
        default='НАША ПРОДУКЦИЯ'
    )

    terms_menu_title = models.CharField(
        'Название "Сроки" в меню',
        max_length=100,
        blank=True,
        default='Сроки'
    )
    terms_section_title = models.CharField(
        'Заголовок раздела "Сроки"',
        max_length=200,
        blank=True,
        default='СРОКИ'
    )

    payment_menu_title = models.CharField(
        'Название "Оплата" в меню',
        max_length=100,
        blank=True,
        default='Оплата'
    )
    payment_section_title = models.CharField(
        'Заголовок раздела "Оплата"',
        max_length=200,
        blank=True,
        default='ОПЛАТА'
    )

    portfolio_menu_title = models.CharField(
        'Название "Портфолио" в меню',
        max_length=100,
        blank=True,
        default='Оборудование'
    )
    portfolio_section_title = models.CharField(
        'Заголовок раздела "Портфолио"',
        max_length=200,
        blank=True,
        default='ОБОРУДОВАНИЕ'
    )
    portfolio_section_subtitle = models.CharField(
        'Подзаголовок раздела "Портфолио"',
        max_length=255,
        blank=True,
        default='Наше оборудование и производственные возможности'
    )

    delivery_menu_title = models.CharField(
        'Название "Доставка" в меню',
        max_length=100,
        blank=True,
        default='Доставка'
    )
    delivery_section_title = models.CharField(
        'Заголовок раздела "Доставка"',
        max_length=200,
        blank=True,
        default='ДВА ВАРИАНТА ДОСТАВКИ'
    )

    contact_menu_title = models.CharField(
        'Название "Контакты" в меню',
        max_length=100,
        blank=True,
        default='Контакты'
    )
    contact_section_title = models.CharField(
        'Заголовок раздела "Контакты"',
        max_length=200,
        blank=True,
        default='КОНТАКТЫ'
    )

    contact_form_title = models.CharField(
        'Заголовок формы',
        max_length=255,
        blank=True,
        default='ОТПРАВЬТЕ ФОРМУ ИЛИ СВЯЖИТЕСЬ С НАМИ САМОСТОЯТЕЛЬНО'
    )
    consent_text = models.CharField(
        'Текст согласия',
        max_length=255,
        blank=True,
        default='Я соглашаюсь с правилами обработки данных'
    )
    submit_button_text = models.CharField(
        'Текст кнопки отправки',
        max_length=100,
        blank=True,
        default='ОТПРАВИТЬ'
    )

    telegram_url = models.URLField(
        'Ссылка на Telegram',
        blank=True
    )
    telegram_button_text = models.CharField(
        'Текст кнопки Telegram',
        max_length=50,
        blank=True,
        default='TELEGRAM'
    )

    whatsapp_url = models.URLField(
        'Ссылка на WhatsApp',
        blank=True
    )
    whatsapp_button_text = models.CharField(
        'Текст кнопки WhatsApp',
        max_length=50,
        blank=True,
        default='WHATSAPP'
    )

    modal_title = models.CharField(
        'Заголовок модального окна',
        max_length=200,
        blank=True,
        default='Рассчитать стоимость'
    )
    modal_submit_button_text = models.CharField(
        'Текст кнопки модального окна',
        max_length=100,
        blank=True,
        default='Отправить'
    )
    footer_text = models.CharField(
        'Текст в подвале',
        max_length=255,
        blank=True,
        default='© 2026 Типография. Все права защищены.'
    )

    portfolio_section_title = models.CharField(
        "Заголовок блока оборудования",
        max_length=255,
        default="СОБСТВЕННОЕ ПРОИЗВОДСТВО"
    )

    portfolio_section_text = models.TextField(
        "Текст блока оборудования",
        blank=True,
        default=(
            "Многие клиенты не знают, что большая часть полиграфических компаний "
            "является посредниками. Они имеют множество центров приема заказов, "
            "но сами не могут отвечать за качество и сроки. А их клиенты каждый раз "
            "переплачивают посредническую комиссию.\n\n"
            "При этом наличие на сайте фото оборудования ничего не значит. "
            "Хотите отличить посредника от реальной типографии, просто спросите у менеджера: "
            "«А можно приехать на ваше производство и увидеть, как печатается продукция..?»"
        )
    )


    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return self.site_name or 'Настройки сайта'
