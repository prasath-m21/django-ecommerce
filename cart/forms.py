# cart/forms.py

from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    """
    Form for adding products to cart with quantity selection.
    """
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        initial=1,
        widget=forms.Select(attrs={
            'class': 'form-select form-select-sm',
            'style': 'width: 80px;'
        })
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
