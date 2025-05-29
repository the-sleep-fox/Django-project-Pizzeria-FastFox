from django.db import models

# Create your models here.

class Questions(models.Model):
    title = models.CharField("Main Question", max_length=100)
    full_text = models.TextField('Question full text')
    date = models.DateTimeField('Publish date')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"