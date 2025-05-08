from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Drug(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=[
                              ('new', 'New'), ('opened', 'Opened')])
    remain = models.IntegerField()
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("drug_list")
