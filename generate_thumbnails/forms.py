from django import forms
from django.core.files.images import get_image_dimensions
from PIL import Image
from io import BytesIO


class ThumbNailImageForm(forms.Form):

    image = forms.ImageField()
    thumbnail_sizes = forms.CharField(widget=forms.Textarea)

    def save(self):
        main_image = YourImageModel.objects.create(image=self.cleaned_data['image'])
        thumbnail_sizes = self.cleaned_data['thumbnail_sizes'].split(',')
        for size_str in thumbnail_sizes:
            width, height = size_str.strip().split('x')
            thumbnail = self.create_thumbnail(main_image, int(width), int(height))
            thumbnail_field = f'thumbnail_{width}x{height}'
            setattr(main_image, thumbnail_field, thumbnail)
        main_image.save()

    def create_thumbnail(self, main_image, width, height):
        image = Image.open(main_image.image)
        image.thumbnail((width, height))
        thumbnail_io = BytesIO()
        image.save(thumbnail_io, format=image.format)
        thumbnail_file = thumbnail_io.getvalue()
        return thumbnail_file

