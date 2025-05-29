from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


# Create your models here.
class Reviews(models.Model):
    anons = models.CharField("Short review", max_length=250)
    full_text = models.TextField('Review full text')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=False, blank=True)

    def __str__(self):
        return self.anons
    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"