from django.contrib.auth.forms import UserChangeForm, ReadOnlyPasswordHashField, UsernameField
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from base.models import Profile


class CustomUserChangeForm(UserChangeForm):

    email = forms.EmailField(label=_("Email"), help_text=_("Enter valid email address"))

    displayname = forms.CharField(label=_("Display Name"), help_text=_("Enter display name"), required=False)

    password = ReadOnlyPasswordHashField(label=_("Password"), help_text=_("Raw passwords are not stored, so there is "
                                                                          "no way to see this user's password, but you "
                                                                          "can change the password using "
                                                                          "<a href=\"/accounts/password_change/\">"
                                                                          "this form</a>."))

    class Meta:
        model = User
        fields = ("username", "email", "displayname", "password")
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profile = Profile.objects.get(user=self.instance)
        self.fields['displayname'].initial = self.profile.display_name
        f = self.fields.get('user_permissions')
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
            self.profile.display_name = self.cleaned_data['displayname']
            self.profile.save()
        return user

    def clean_password(self):
        return self.initial["password"]
