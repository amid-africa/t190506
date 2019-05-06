from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

from .forms import PricelistProductForm
from .models import Product, Pricelist, PricelistProduct


"""Generic CreateView to create products"""
class CreateProductView(CreateView):
    template_name = 't190506/product.html'
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('create_product')


"""Generic CreateView to create pricelists"""
class CreatePricelistView(CreateView):
    template_name = 't190506/pricelist.html'
    model = Pricelist
    fields = '__all__'
    success_url = reverse_lazy('pricelist_add_product')

    # on save, set success_url to add product to the created list
    def form_valid(self, form):
        pricelist = form.save()
        self.success_url = reverse_lazy('pricelist_add_product',
                                        kwargs={'pk': pricelist.pk})
        return super(CreatePricelistView, self).form_valid(form)


"""Add our products to a pricelist"""
class PricelistProductView(CreateView):
    template_name = 't190506/pricelistproduct.html'
    model = PricelistProduct
    form_class = PricelistProductForm
    pricelist = None

    # Set the success url to be the current url
    def get_success_url(self):
        return self.request.path

    # Set the pricelist form field from the pricelist pk
    def get_initial(self):
        self.pricelist = get_object_or_404(Pricelist, pk=self.kwargs.get('pk'))
        return {
            'pricelist':self.pricelist,
        }

    #Add pricelist data to the context
    def get_context_data(self, *args, **kwargs):
        context = super(PricelistProductView, self).get_context_data(*args, **kwargs)
        context['pricelist'] = self.pricelist
        return context
