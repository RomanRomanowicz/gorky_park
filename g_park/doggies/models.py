from django.db import models

# Create your models here.

class ViewDoggies(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    opening_hours = models.CharField(max_length=255, blank=True)
    technical_characteristics = models.TextField(blank=True)
    produced = models.TextField(blank=True)

    def __str__(self):
        return self.title


class ReportingDoggies(models.Model):
    visitors = models.IntegerField(blank=True, null=True)
    tickets = models.IntegerField(blank=True, null=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"количество посетителей: {self.visitors},  " \
               f"количество проданых билетов : {self.tickets}"