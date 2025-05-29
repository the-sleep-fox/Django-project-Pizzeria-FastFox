from django.db import models

# Create your models here.

class Offers(models.Model):
    specialist_name = models.CharField("Name", max_length=50)
    describing = models.TextField('Describing')
    requirements = models.TextField('Requirements')
    salary = models.CharField('Salary', max_length=100)

    def __str__(self):
        return self.specialist_name
    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"