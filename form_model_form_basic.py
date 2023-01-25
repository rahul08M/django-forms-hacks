import os    # import os library
from django import forms    # import forms from django
from django.utils.translation import gettext_lazy as _   

from django.contrib.auth.models import User    # import User model from django.contrib.auth.models


class BaseUserModelForm(forms.ModelForm):    # Defining the class "BaseUserModelForm" with inheritance from  forms.ModelForm

    class Meta:    # Define the meta class
        model = User    # Assign the model "User" to meta class
        fields = ('first_name', 'last_name', 'email')    # Assign the fields first_name, last_name and email

        labels = {    # Defining labels for fields
            'first_name': _('First Name'),    # Field first_name label
            'last_name': _('Last/Sur Name'),    # Field last_name label
            'email': _('Email Address'),    # Field email label
        }

        help_texts = {    # Defining help_texts for fields
            'email': _('Email address must be classic.'),    # Field email help_text
        }
