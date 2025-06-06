from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    # Ajout d'un champ texte pour entrer le nom de la catégorie
    category_name = forms.CharField(
        max_length=100,
        required=True,
        label='Category',
        widget=forms.TextInput(
            attrs={'placeholder': 'e.g. Clothing', 'class': 'form-control'}
        )
    )

    class Meta:
        model = Product
        # Exclusion du champ 'category' car il est géré via 'category_name'
        fields = ['product_id', 'name', 'sku', 'price', 'quantity', 'supplier','image', 'category_name']
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
            'image': 'Image',
        }
        widgets = {
            'product_id': forms.NumberInput(
                attrs={'placeholder': 'e.g. 1', 'class': 'form-control'}
            ),
            'name': forms.TextInput(
                attrs={'placeholder': 'e.g. shirt', 'class': 'form-control'}
            ),
            'sku': forms.TextInput(
                attrs={'placeholder': 'e.g. S12345', 'class': 'form-control'}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'e.g. 19.99', 'class': 'form-control'}
            ),
            'quantity': forms.NumberInput(
                attrs={'placeholder': 'e.g. 10', 'class': 'form-control'}
            ),
            'supplier': forms.TextInput(
                attrs={'placeholder': 'e.g. ABC Corp', 'class': 'form-control'}
            ),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
        }

    def save(self, commit=True):
        # Récupérer l'instance du produit sans l'enregistrer immédiatement
        product = super().save(commit=False)
        
        # Récupérer ou créer la catégorie en fonction du nom saisi
        category_name = self.cleaned_data['category_name']
        category, created = Category.objects.get_or_create(
            name=category_name.strip()
        )
        
        # Associer la catégorie au produit
        product.category = category
        
        # Enregistrer le produit si commit est True
        if commit:
            product.save()
        
        return product