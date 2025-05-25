from django.db import models

# Create your models here.

class Promocodes(models.Model):
    title = models.CharField("Name", max_length=50)
    full_text = models.TextField('Question full text')
    date = models.DateTimeField('Expire date')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Promo-code"
        verbose_name_plural = "Promo-codes"