import os

from django.utils.translation import gettext_lazy as _

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def validate_pdf_file_extension(value):  # method validate pdf file.
    ext = os.path.splitext(value.name)[1]  # split the file object
    valid_extensions = ['.pdf'] 

    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Unsupported file extension. Allowed only PDF.'))  # raise the form validation error message


class BaseValidationForm(forms.Form):

    """
    You can add various type's of form validations
    1. Regex validations.
    2. File type validations.
    """

    full_name = forms.CharField(
        label=_('Full Name'), required=True,
        validators=[RegexValidator('^([A-Za-z ])+$', message=_('Please enter a valid name.'))]  # check if first name contains only alphabets
    )
    contact_number = forms.CharField(
        label=_('Contact/Mobile No.'),
        validators=[
            RegexValidator('^([0-9])+$', message=_('Please enter a valid contact number.'))  # check if contact number contains only numbers
        ]
    )
    pdf_file = forms.FileField(
        label=_('PDF File'),
        validators=[validate_pdf_file_extension]  # check if uploaded file's extension is PDF.
    )
