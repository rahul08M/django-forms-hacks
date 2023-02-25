from django import forms
from django.utils.translation import gettext as _



class BaseHTMLAttrsForm(forms.Form):

    """
    You can add html attributes into Django forms in two ways.
    1. Adding directly into the form Field using widget
    2. Adding attrs into form __init__ method
    """

    # adding html attributes
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'css-class',
                'placeholder': _('First Name')
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(BaseHTMLAttrsForm, self).__init__(*args, **kwargs)

        # adding html attributes
        self.fields['first_name'].widget.attrs['class'] = 'css-class'
        self.fields['first_name'].widget.attrs['placeholder'] = _('First Name')
        
