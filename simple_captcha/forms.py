from django import forms
from captcha.fields import CaptchaField


class BaseCaptchaForm(forms.Form):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'css-class',
                'placeholder': 'First Name'
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'css-class',
                'placeholder': 'Last Name'
            }
        )
    )

    captcha = CaptchaField()  # django simple captcha's captcha field

    def __init__(self, *args, **kwargs):
        super(BaseCaptchaForm, self).__init__(*args, **kwargs)
