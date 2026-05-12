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
        