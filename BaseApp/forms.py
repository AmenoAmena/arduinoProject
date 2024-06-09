from django import forms
from .models import item, sensorImage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=40,label='Kullanıcı adı',widget=forms.TextInput(attrs={
        'placeholder':'Username: ',
        'autocomplete':'off'
        }))
    password1 = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={
        'placeholder': 'Password: ',
        'autocomplete':'off'
        }))
    password2 = forms.CharField(label='Yeniden Şifre', widget=forms.PasswordInput(attrs={
        'placeholder': 'Password: ',
        'autocomplete':'off'
        }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class itemForm(forms.ModelForm):

    class Meta:
        model = item
        fields = ("name", "image", "number")
        labels = {
            'name': 'Sensor name',
            'image': 'Sensor type',
            'number': 'Sensor number'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].queryset = sensorImage.objects.all()
        self.fields['image'].label_from_instance = lambda obj: obj.name
        self.fields['image'].empty_label = 'Model Seçiniz'

        self.fields['name'].widget.attrs['autocomplete'] = 'off'
        self.fields['image'].widget.attrs['autocomplete'] = 'off'
        self.fields['number'].widget.attrs['autocomplete'] = 'off'
        
        placeholders = {
            'name': 'Sensor name',
            'image': 'Sensor type',
            'number': 'Sensor number'
        }

        for field_name, placeholder_text in placeholders.items():
            self.fields[field_name].widget.attrs['placeholder'] = placeholder_text

