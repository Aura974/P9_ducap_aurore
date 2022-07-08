from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=128, verbose_name="Titre")
    description = models.CharField(max_length=2048, blank=True, verbose_name="Description")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128, verbose_name="Titre")
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    body = models.CharField(max_length=8192, blank=True, verbose_name="Commentaire")
    user = user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
