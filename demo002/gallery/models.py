from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    user_update = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    description = models.CharField(
        max_length = 128,
        help_text = "Category Description",
        unique = True
    )
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return "{}".format(self.description)

class Item(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=128, unique=True, help_text="SubCategory Description")
    def __str__(self):
        return "{}".format(self.description)
