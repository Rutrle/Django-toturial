from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    # max_length = required, if not there, migrations won't work and reurn error
    title = models.CharField(max_length=120)
    # null = True - makes the vallue optional,
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    # blank deals with how field is rendered when filling it in (optional/mandatory), null deals with database - if this value muset be there
    summary = models.TextField(blank=True, null=False)
    # new field, possibilities: 1) delete database and make new one, 2) null = True -> in all old data this field will be empty 3) default = True => sets default value  to the value given 4) give info to python during  making migrations
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"my_id": self.id})



