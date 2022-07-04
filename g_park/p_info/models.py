from django.db import models

# Create your models here.
class InfoPark(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title


class InfoHistory(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title


class InfoPersonnel(models.Model):
    function = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)

    def __str__(self):
        return f"Ответственый за аттракцион: " \
               f" {self.function}  ФИО: {self.name} {self.telephone}"
