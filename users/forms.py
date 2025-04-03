from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False,
                                   help_text='Необязательное поле. Введите ваш номер телефона.', label='Телефон')
    username = forms.CharField(max_length=50, required=True, help_text='', label='Имя пользователя')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'phone_number', 'country')
        label = {
            'username': 'Имя пользователя', 'phone_number': 'Телефон'
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять только из цифр')
        return phone_number
