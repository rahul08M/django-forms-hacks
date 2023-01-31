from django import forms


class BaseSelect2Form(forms.Form):

    RANDOM_CHOICES = (
        ('Naruto', 'Naruto'),
        ('Kiba', 'Kiba'),
        ('Kakashi', 'Kakashi'),
        ('Obito', 'Obito'),
        ('Rin', 'Rin'),
    )

    multiple_choices = forms.MultipleChoiceField(choices=RANDOM_CHOICES)

    def __init__(self, *args, **kwargs):
        super(BaseSelect2Form, self).__init__(*args, **kwargs)

        # adding html attributes
        self.fields['multiple_choices'].widget.attrs['class'] = 'select2'
