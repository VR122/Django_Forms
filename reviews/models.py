from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    review = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.user_name} - {self.rating}'