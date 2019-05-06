from django import forms

from .models import Product, PricelistProduct


"""Pricelist Product create"""
class PricelistProductForm(forms.ModelForm):

    class Meta:
        model = PricelistProduct
        fields = '__all__'
        widgets = {
            'pricelist': forms.HiddenInput,
        }

    def __init__(self, *args, **kwargs):
        super(PricelistProductForm, self).__init__(*args, **kwargs)

        # Get the inital values set in the view
        inital = kwargs.get('initial')

        # Get the pricelist we are using
        pricelist = inital.get('pricelist')

        # Get a 'value list' of products already in the price list
        existing = PricelistProduct.objects.filter(pricelist=pricelist).values_list('product')

        # Override the product query set with a list of product excluding those already in the pricelist
        self.fields['product'].queryset = Product.objects.exclude(id__in=existing)
