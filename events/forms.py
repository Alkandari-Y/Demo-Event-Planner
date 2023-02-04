from django import forms
from events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ["organizer"]
        widgets = {"start_date": forms.DateTimeInput(attrs={"type": "date"})}
