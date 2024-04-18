from django import forms
from .models import item, sensorImage

class itemForm(forms.ModelForm):

    class Meta:
        model = item
        fields = ("name", "image", "number")
        labels = {
            'name': 'Sensör İsmi',
            'image': 'Sensör Tipi',
            'number': 'Sensor Sayısı'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the representation of the image field choices
        self.fields['image'].queryset = sensorImage.objects.all()
        self.fields['image'].label_from_instance = lambda obj: obj.name
        self.fields['image'].empty_label = 'Model Seçiniz'