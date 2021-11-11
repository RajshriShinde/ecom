from celery import shared_task
from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from ecom import settings
from .models import *


@shared_task
def send_mail_to_users(subject, message, from_email):
    emails = list(get_user_model().objects.all().values_list('email', flat=True))
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=emails,
        fail_silently=True,
    )


@shared_task
def send_email_to_staff_users():
    staff_emails = list(get_user_model().objects.filter(is_staff=True).values_list("email", flat=True))
    products_count = Product.objects.count()
    variants_count = Variant.objects.count()
    customer_count = get_user_model().objects.filter(is_staff=False, is_superuser=False).count()

    categories = Category.objects.all()
    category_products_count = [f"{category.title}:{category.all_products.count()}" for category in categories]
    no_of_products = '\n'.join(category_products_count)

    send_mail(
        subject="Daily status",
        message=f"Product count is: {products_count}\n Variants count is : {variants_count}\n Number of Customers are:\
                                     {customer_count} \n Number of Products for each category: \n {no_of_products}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=staff_emails,
        fail_silently=True,
    )







