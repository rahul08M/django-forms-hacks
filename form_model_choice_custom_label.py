from django import forms
from apps.category.models import Category  # import your db model (Category is for ref.)


class SelectWithOptionAttribute(forms.Select):

    """Class to override the base form Select"""
    # ref : https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#module-django.forms.widgets

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):

        if isinstance(label, dict):
            opt_attrs = label.copy()
            label = opt_attrs.pop('label')
        else:
            opt_attrs = {}
        option_dict = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        for key, val in opt_attrs.items():
            option_dict['attrs'][key] = val
        return option_dict


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
