from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Nom d'utilisateur", "style": "text-align: center;"})
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Mot de passe", "style": "text-align: center;"})
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirmer mot de passe", "style": "text-align: center;"})


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control",
             "placeholder": "Nom d'utilisateur",
             "style": "text-align: center;"}
            )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control",
             "placeholder": "Mot de passe",
             "style": "text-align: center;"}
            )
