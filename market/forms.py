from django import forms
from string import Template
from django.utils.safestring import mark_safe
from .models import Products
from django.forms import ModelForm, fields, TextInput, widgets, Textarea, ImageField, FileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# class PictureWidget(forms.widgets.Widget):
#     def render(self,attrs={
#                 'class':'form-control',
#                 'placeholder':'Product image'
#     }, **kwargs):
#         html =  Template("""<img src="$link"/>""")
#         return mark_safe(html.substitute(link=value))

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['title', 'prod_decription', 'prod_image', 'prod_price']

        widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Product name'
            }),
            # 'prod_image':ImageField(widget=PictureWidget),
            'prod_decription':Textarea(attrs={
                'class':'form-control',
                'placeholder':'Product description'
            }),
            'prod_image':FileInput(attrs={
                'class':'form-control-file'
            }),
            'prod_price':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Product name'
            }),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]