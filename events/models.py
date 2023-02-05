from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(
        upload_to="events", blank=True, default="events/default.png"
    )
    description = models.CharField(max_length=255)
    number_seats = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                limit_value=10,
                message="Minimum number of seats must be equal to or greater than 10",
            )
        ]
    )
    organizer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events_created"
    )
    start_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
