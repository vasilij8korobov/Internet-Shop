from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return self.validate_no_bad_words(name)

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return self.validate_no_bad_words(description)

    def validate_no_bad_words(self, value):
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in bad_words:
            if word.lower() in value.lower():
                raise forms.ValidationError(f"Слово '{word}' запрещено.")
        return value
