from django.db import models
from house.models import TimeStampedModel
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Review(TimeStampedModel):

    review = models.TextField()
    customer_service = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    cleanliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    location = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    suitable_price = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    house = models.ForeignKey(
        "house.House", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.house}"
    
    def avgRating(self):
        avg = (self.customer_service
            + self.cleanliness
            + self.location
            + self.suitable_price) / 4
        return round(avg, 2)
    
    avgRating.short_description = "Avg."
