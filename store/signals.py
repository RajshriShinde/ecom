from .models import *
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .task import send_mail_to_users
from ecom import settings


@receiver(pre_save, sender=Product)
def log_product_will_be_created(instance, **kwargs):
    print(f"Product {instance.title} will be created")


@receiver(post_save, sender=Product)
def send_mail_on_product_created(instance, created=False, **kwargs):
    if created:
        print(f"Product {instance.title} added successfully")
        send_mail_to_users.delay("New product added", f"{instance.title} \n {instance.description}"
                                                    , settings.EMAIL_HOST_USER)


@receiver(pre_delete, sender=Product)
def log_product_will_be_deleted(instance, **kwargs):
    print(f"Product {instance.title} will be deleted")


@receiver(post_delete, sender=Product)
def log_product_deleted(instance, **kwargs):
    print(f"Product {instance.title} deleted")


@receiver(pre_save, sender=Variant)
def log_variant_will_be_created(instance, **kwargs):
    print(f"Variant {instance.title} will be created")


@receiver(post_save, sender=Variant)
def log_on_variant_created(instance, created=False, **kwargs):
    if created:
        print(f"Variant {instance.title} added successfully")


@receiver(pre_delete, sender=Variant)
def log_variant_will_be_deleted(instance, **kwargs):
    print(f"Variant {instance.title} will be deleted")


@receiver(post_delete, sender=Variant)
def log_variant_deleted(instance, **kwargs):
    print(f"Variant {instance.title} deleted")


@receiver(pre_save, sender=Image)
def log_image_will_be_added(instance, **kwargs):
    print(f"Image {instance.alt_txt} will be created")


@receiver(post_save, sender=Image)
def log_on_image_added(instance, created=False, **kwargs):
    if created:
        print(f"Image {instance.alt_txt} added successfully")


@receiver(pre_delete, sender=Image)
def log_image_will_be_deleted(instance, **kwargs):
    print(f"Image {instance.alt_txt} will be deleted")


@receiver(post_delete, sender=Image)
def log_image_deleted(instance, **kwargs):
    print(f"Image {instance.alt_txt} deleted")


@receiver(pre_save, sender=Collection)
def log_collection_will_be_created(instance, **kwargs):
    print(f"Collection {instance.title} will be created")


@receiver(post_save, sender=Collection)
def log_on_collection_created(instance, created=False, **kwargs):
    if created:
        print(f"Collection {instance.title} added successfully")


@receiver(pre_delete, sender=Collection)
def log_collection_will_be_deleted(instance, **kwargs):
    print(f"Collection {instance.title} will be deleted")


@receiver(post_delete, sender=Collection)
def log_collection_deleted(instance, **kwargs):
    print(f"Collection {instance.title} deleted")


@receiver(pre_save, sender=Category)
def log_category_will_be_created(instance, **kwargs):
    print(f"Category {instance.title} will be created")


@receiver(post_save, sender=Category)
def log_on_category_created(instance, created=False, **kwargs):
    if created:
        print(f"Category {instance.title} added successfully")


@receiver(pre_delete, sender=Category)
def log_category_will_be_deleted(instance, **kwargs):
    print(f"Category {instance.title} will be deleted")


@receiver(post_delete, sender=Category)
def log_category_deleted(instance, **kwargs):
    print(f"Category {instance.title} deleted")







