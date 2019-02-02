from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from base.models import Profile
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(
        label=_("Email"),
        help_text=_("Enter valid email address"),
    )

    displayname = forms.CharField(
        label=_("Displayname"),
        help_text=_("Enter displayname."),
        required=False,
    )

    class Meta:
        model = User
        fields = ("username", "email", "displayname", "password1", "password2",)
        field_classes = {'username': UsernameField}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            profile = Profile(display_name=self.cleaned_data["displayname"])
            profile.user = user
            profile.save()
        return user