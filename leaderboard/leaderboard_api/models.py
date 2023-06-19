from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, validators=[RegexValidator(r'^[a-zA-Z]+$')])
    score = models.IntegerField(default=0)
    age = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    address = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name
    