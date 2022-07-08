from django import forms
from feeds import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ["headline", "rating", "body"]
