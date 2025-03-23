from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from .models import Product


class ProductForm(forms.ModelForm):
    price = forms.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем CSS-классы к каждому полю для стилизации
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return self.check_forbidden_words(name)

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return self.check_forbidden_words(description)

    # def clean_price(self):
    #     price = self.cleaned_data['price']
    #     if price is not None and price < 0:
    #         raise ValidationError("Цена не может быть отрицательной или отсутствовать.")
    #     return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5 MB
                raise ValidationError("Размер изображения не может превышать 5 МБ.")
            if not image.content_type in ['image/jpeg', 'image/png']:
                raise ValidationError("Допустимые форматы изображения: JPEG, PNG.")
        return image

    def check_forbidden_words(self, value):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in value.lower():
                raise ValidationError(f"Слово '{word}' запрещено к использованию.")
        return value
