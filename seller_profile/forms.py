from django import forms 
from catalog.models import Product, Category
from mptt.forms import TreeNodeChoiceField

class CategoryCreateForm(forms.ModelForm):
    name = forms.CharField(label='название категории')
    description = forms.CharField(label='описани категории', widget=forms.Textarea)
    image = forms.ImageField(label='фотка категории')
    parent = TreeNodeChoiceField(queryset=Category.objects.all(), required=False, empty_label='родителя нет')

    class Meta:
        model = Category
        fields = ['name', 'description', 'image', 'parent']

class CategorySelectForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='выбери категорию')

    class Meta:
        model = Category
        fields = ['category']

class ProductCreateForm(forms.ModelForm):
    description = forms.CharField(label='Описание продукта',widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'avaible', 'image', 'category']
        labels = {
            'name': 'Название продукта',
            'price': 'Цена товара',
            'stock': 'Количество на складе',
            'available': 'Сделать доступным',
            'image': 'Фотография',
        }
