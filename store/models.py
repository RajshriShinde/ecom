from django.db import models


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, related_name='products')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return "%s" % self.title


class Variant(models.Model):
    image = models.OneToOneField('Image', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products', null=True)
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    available_for_sale = models.BooleanField(max_length=None)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s " % self.title


class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, related_name='images')
    source = models.ImageField(upload_to="product_pics/", max_length=100)
    alt_text = models.CharField(max_length=100)
    uploaded_at = models.DateField(auto_now=True)

    def __str__(self):
        return "%s " % self.alt_text


class Collection(models.Model):
    products = models.ManyToManyField('Product', through='ProductCollection', related_name='collections')
    title = models.CharField(max_length=100)
    published = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return "%s " % self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return "%s " % self.title

    @property
    def get_all_subcategories(self):
        direct_subcategories = self.subcategories
        children_subcategories = [subcategory.get_all_subcategories for subcategory in direct_subcategories]

        return direct_subcategories(*children_subcategories)

    @property
    def all_variants(self):
        category_ids = list(self.get_all_subcategories.values_list('id', flat=True))
        category_ids.append(self.id)
        return Variant.objects.filter(product__category__id__in=category_ids)


class ProductCollection(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.product




