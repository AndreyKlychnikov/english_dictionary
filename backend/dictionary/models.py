from accounts.models import User
from django.db import models


class Source(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return self.name


class Word(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    original = models.CharField(max_length=500)
    translation = models.CharField(max_length=500)
    definition = models.CharField(max_length=1000, blank=True, default="")
    context = models.CharField(max_length=1000, blank=True, default="")

    def __str__(self):
        return f"{self.original} - {self.translation}"
