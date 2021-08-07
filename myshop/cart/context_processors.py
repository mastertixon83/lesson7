from .cart import Cart


def cart(request):
    """Контекстный процессор, добавляет в контекст объект корзины

    Как мы уже говорили, контекстный процессор – это обычная функция, кото-
рой в качестве аргумента передается объект запроса, request, и которая должна
возвращать словарь. Этот словарь будет добавляться в контекст любого шабло-
на, работающего с контекстом типа RequestContext. В нашей функции мы ини-
циируем корзину, передавая в конструктор объект текущего запроса, и добав-
ляем в контекст в виде переменной cart.
Откройте файл settings.py проекта и допишите cart.context_processors.cart
в раздел context_processors настройки TEMPLATES таким образом:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'cart.context_processors.cart',
            ],
        },
    },
]
    """
    return {'cart': Cart(request)}
