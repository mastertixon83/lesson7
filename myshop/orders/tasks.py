from celery import task
from django.core.mail import send_mail
from .models import Order

# celery -A celery_main beat -s celerybeat-schedule.db --loglevel INFO
# celery -A config --loglevel INFO

@task
def order_created(order_id):
    """Задача отправки email-уведомлений при успешном оформлении заказа"""
    order = Order.objects.get(pk=order_id)
    subject = f'Order nr.{order.id}'
    message = f'Dear {order.first_name}, \n\nYou have succesfully placed an order. You order is {order.id}'
    mail_sent = send_mail(
                            subject,
                            message,
                            'tikhonov2011@mail.ru',
                            [order.email]
    )
    return mail_sent
