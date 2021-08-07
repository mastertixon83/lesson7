from django.db import models
from shop.models import Product


class Order(models.Model):
    """Заказ"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.pk}'

    def get_total_cost(self):
        """получить общую стоимость товаров в заказе"""
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Для связи заказа с покупаемым товаром"""
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.pk}'

    def get_cost(self):
        """Подсчет общей стоимости позиции в корзине"""
        return self.price * self.quantity
