from django.db import models

class Partners(models.Model):
    name = models.CharField(max_length=100)
    image= models.ImageField(upload_to='images/')
    link = models.URLField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"