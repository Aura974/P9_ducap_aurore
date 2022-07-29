from django import forms


class UnfollowsForm(forms.Form):
    unfollows = forms.BooleanField(widget=forms.HiddenInput, initial=True)
