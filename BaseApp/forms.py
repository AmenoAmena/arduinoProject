from django import forms
from .models import item, sensorImage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=40,label='Kullanıcı adı',widget=forms.TextInput(attrs={
        'placeholder':'Kullanıcı Adı',
        'autocomplete':'off'
        }))
    password1 = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={
        'placeholder': 'Şifre',
        'autocomplete':'off'
        }))
    password2 = forms.CharField(label='Yeniden Şifre', widget=forms.PasswordInput(attrs={
        'placeholder': 'Şifreyi doğrulayın',
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