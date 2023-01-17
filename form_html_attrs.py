from django import forms


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
                'placeholder': 'First Name'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(BaseHTMLAttrsForm, self).__init__(*args, **kwargs)

        # adding html attributes
        self.fields['first_name'].widget.attrs['class'] = 'css-class'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        
