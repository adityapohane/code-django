from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    # id = models.AutoField(primary_key=True)# you don't have to actually set this field django automatically sets autoincrementing field and primary key
    title = models.CharField(max_length=255)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()
        # kwargs - key word arguments

    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])
