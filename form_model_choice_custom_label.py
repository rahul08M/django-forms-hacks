from django import forms
from apps.category.models import Category  # import your db model (Category is for ref.)


class CustomModelChoiceField(forms.ModelChoiceField):
    
    """Class to override the model choice display label."""
    # You can also add extra html attrs, in this example I have added the data attribute
    
    widget = SelectWithOptionAttribute

    def label_from_instance(self, obj):
        return {
            'label': super().label_from_instance(obj), 'data-label': obj.id(),
        }


class BaseModelChoiceForm(forms.Form):

    category = CustomModelChoiceField(queryset=Category.objects.all())

    def __init__(self, *args, **kwargs):
        super(BaseModelChoiceForm, self).__init__(*args, **kwargs)
