from django.db.models.functions import Concat
from .models import *
from django.db.models import Value as V, F
from django.db.models.signals import pre_delete
from django.dispatch import receiver


@receiver(pre_delete, sender=Product)
def list_of_product(sender, **kwargs):
    return list(Product.objects.values('title', 'description', 'created_at', 'updated_at').annotate(_images=F('images')))


def list_of_variant():
    return list(Variant.objects.values('created_at', 'updated_at', 'available_for_sale', 'price', 'image')
                               .annotate(_title=Concat('product__title', V(" "), 'title')))


def list_of_collections():
    return list(Collection.objects.values('title', 'published', 'updated_at'))


def list_of_product_of_collections(coll_id):
    return list(Product.objects.values('title', 'description', 'created_at', 'updated_at').filter(collections=coll_id)
                               .annotate(_images=F('images')))


def list_of_variants_of_collection(coll_id):
    return list(Variant.objects.values('created_at', 'updated_at', 'available_for_sale', 'price', 'image')
                               .annotate(_title=Concat('product__title', V(" "), 'title'))
                               .filter(product__collections=coll_id))


def list_of_variants_of_category(category_id):
    category = Category.objects.get(id=category_id)
    return list(category.all_variants.values('created_at', 'updated_at', 'available_for_sale', 'price', 'image')
                        .annotate(_title=Concat('product__title', V(" "), 'title')))
