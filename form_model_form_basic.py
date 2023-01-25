import os
from django import forms
from django.utils.translation import gettext_lazy as _https://github.com/rahul08M/django-forms-hacks/blob/main/form_model_form_basic.py

from django.contrib.auth.models import User


class BaseUserModelForm(forms.ModelForm):

    """
    Basic model form which connects with the User model
    From has basic Meta class attributes, such as labels and help texts
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last/Sur Name'),
            'email': _('Email Address'),
        }

        help_texts = {
            'email': _('Email address must be classic.'),
        }

    def clean_email(self, email):  # Clean method to validate the duplicate email address.

        if User.objects.filter(email__iexact=email):  # iexact check for case-insensitive conditions.
            raise forms.ValidationError(_(f"{email} already exists."))
        return email
