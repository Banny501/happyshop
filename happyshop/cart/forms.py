from django import forms


class CartAddProductForm(forms.Form):
    product = forms.SlugField()
