from django.shortcuts import render
from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart
from .tasks import order_created


def order_create(request):
    """Обработчик создания заказа

    В этом обработчике мы получаем объект корзины с помощью выражения
cart = Cart(request). В зависимости от метода выполняем следующие действия:
при получении GET-запроса инициируем форму OrderCreateForm и переда-
ем ее в шаблон orders/order/create.html;
при получении POST-запроса валидируем данные формы. Если они кор-
ректны, записываем новый заказ в базу данных с помощью выражения
order = form.save(). После этого проходим по всем товарам корзины и создаем
для каждого объект OrderItem. Наконец, очищаем форму, хранящую-
ся в сессии, и формируем страницу ответа из шаблона orders/order/created.html.
    """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            # Очищаем корзину
            cart.clear()
            #Запуск асинхронной задачи
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
