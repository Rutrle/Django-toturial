from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #max_length = required, if not there, migrations won't work and reurn error
    description = models.TextField(blank = True, null = True) #null = True - makes the vallue optional, 
    price = models.DecimalField(decimal_places = 2, max_digits = 10000)
    summary = models.TextField(blank=True, null=False)#blank deals with how field is rendered when filling it in (optional/mandatory), null deals with database - if this value muset be there
    featured = models.BooleanField(default = False) # new field, possibilities: 1) delete database and make new one, 2) null = True -> in all old data this field will be empty 3) default = True => sets default value  to the value given 4) give info to python during  making migrations