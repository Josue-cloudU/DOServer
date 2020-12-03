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

class Cundina(BaseModel):
    descripcion = models.CharField(
        max_length = 128,
        help_text = "Cundina Descripcion",
        unique = True
    )
    cantahorro = models.IntegerField()
    nparticipantes = models.IntegerField()
    class Meta:
        verbose_name_plural = "Cundinas"
    def __str__(self):
        return "{}".format(self.descripcion)
