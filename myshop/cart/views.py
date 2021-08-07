from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    """Обработчик добавления товара в корзину

    Мы обернули функцию cart_add() декоратором require_POST, чтобы обратиться
    к ней можно было только методом POST. Обработчик принимает ID товара
    в качестве аргумента, по которому мы получаем объект Product из базы данных.
    Для работы с корзиной создаем форму CartAddProductForm и, если она валидна,
    добавляем или обновляем сведения по товару. В конце перенаправляем пользователя
    на URL с названием cart_detail.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    """Обработчик удаления товара из корзины"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    """Обработчик вывода списка товаров в корзине

    Данный обработчик будет отображать корзину, основываясь на данных,
    сохраненных в сессии request.session

    Теперь мы будем создавать объект формы CartAddProductForm для каждого то-
вара в корзине, чтобы пользователь мог сохранить новое количество единиц.
Мы инициализируем форму, передавая текущее количество и значение update,
равное True. Таким образом, когда пользователь отправит форму на сервер в об-
работчик cart_add, старое значение количества товаров заменится на новое
    """
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True}
        )
    return render(request, 'cart/detail.html', {'cart': cart})
