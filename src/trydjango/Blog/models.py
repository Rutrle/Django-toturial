from django.db import models
from django.urls import reverse
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        # return reverse("blog", kwargs={"my_id": self.id})
        return (f"articles/{self.id}/")


class Course(models.Model):
    title = models.CharField(max_length=120)
