from django.db import models


# Create your models here.
class Palindroma(models.Model):
    palabra = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Palindromas"

    def __str__(self):
        return f"{self.palabra}"

    def __unicode__(self):
        return self.palabra
