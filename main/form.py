from django import forms

from main.models import Product, Version

forbidden_words = 'казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар'


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'photo', 'category', 'owner')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data in forbidden_words:
            raise forms.ValidationError('Запрещенный продукт')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        if cleaned_data in forbidden_words:
            raise forms.ValidationError('Запрещенное описание продукта')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    model = Version
    fields = ('name_version', 'name_current_version',)

    class Meta:
        model = Version
        fields = '__all__'


