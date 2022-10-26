from django.db import models

# Create your models here.


class Guest(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    attending = models.BooleanField(blank=True)
    meal = models.CharField(max_length=50, default="None")
    comments = models.CharField(max_length=500, default="None")
    plus_one = models.BooleanField(default=False)
    group = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"


class PlusOneGuest(Guest):
    invited_guest = models.OneToOneField("Guest", on_delete=models.PROTECT, primary_key=True, related_name="plus_one_guest")


class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=1000)
