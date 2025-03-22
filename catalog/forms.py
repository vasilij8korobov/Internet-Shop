from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return self.check_forbidden_words(name)

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return self.check_forbidden_words(description)

    def check_forbidden_words(self, value):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in value.lower():
                raise forms.ValidationError(f"Слово '{word}' запрещено к использованию.")
        return value
