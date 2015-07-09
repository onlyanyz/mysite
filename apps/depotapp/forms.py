from django import forms

class ProductForm(forms.Form):
    title=forms.CharField(max_length=100)
    description=forms.CharField(widget=forms.Textarea)
    image_url=forms.CharField(max_length=200)
    price=forms.DecimalField(max_digits=8,decimal_places=2)