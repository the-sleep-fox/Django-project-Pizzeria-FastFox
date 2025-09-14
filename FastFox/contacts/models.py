from django.db import models

class Workers(models.Model):
    name = models.CharField("Name", max_length=100)
    job_description = models.TextField("Job Description")
    photo = models.ImageField("Photo", upload_to="workers_photos/", null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

