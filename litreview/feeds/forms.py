from django import forms
from feeds import models
from django.forms.widgets import ClearableFileInput


class MyClearableFileInput(ClearableFileInput):
    initial_text = "Image actuelle"
    input_text = "Modification"
    clear_checkbox_label = "Effacer"


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True, required=False)

    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]
        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "image": MyClearableFileInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields["title"].widget.attrs.update(
            {"class": "form-control", }
            )


class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True, required=False)

    class Meta:
        model = models.Review
        fields = ["headline", "rating", "body"]
        widgets = {
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        RATES = [(x, x) for x in range(0, 6)]

        self.label_suffix = ""
        self.fields["headline"].widget.attrs.update(
            {"class": "form-control", }
            )
        self.fields["rating"] = forms.ChoiceField(choices=RATES, widget=forms.RadioSelect)
        self.fields["rating"].label = "Note"
