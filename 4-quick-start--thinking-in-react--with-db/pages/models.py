from django.db import models

from django_extensions.db.fields import AutoSlugField


class NaturalKeyManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)


class Category(models.Model):
    name = models.CharField("category name", max_length=255)
    slug = AutoSlugField(populate_from=["name"], editable=True)

    objects = NaturalKeyManager()

    class Meta:
        verbose_name_plural = "categories"

    def natural_key(self):
        return (self.slug,)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("product name", max_length=255)
    slug = AutoSlugField(populate_from=["name"], editable=True)
    price = models.DecimalField(
        "product price", decimal_places=2, max_digits=5
    )
    stocked = models.BooleanField("is product in stock", default=False)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )

    objects = NaturalKeyManager()

    def natural_key(self):
        return (self.slug,)

    def __str__(self):
        return self.name
