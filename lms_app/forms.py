from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'})
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title' ,
            'author' ,
            'price',
            'photo_book',
            'photo_author' ,
            'Number_of_pages' ,
            'retal_price_per_day' ,
            'retal_period',
            'available',
            'status' ,
            'Category' ,
            'total_rental',

        ]
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author' : forms.TextInput(attrs={'class' : 'form-control'}),
            'price': forms.TextInput(attrs={'class' : 'form-control'}),
            'photo_book': forms.FileInput(attrs={'class' : 'form-control'}),
            'photo_author' : forms.FileInput(attrs={'class' : 'form-control'}),
            'Number_of_pages' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'retal_price_per_day' : forms.NumberInput(attrs={'class' : 'form-control', 'id':'rental_price'}),
            'retal_period' :forms.NumberInput(attrs={'class' : 'form-control', 'id':'rental_days'}),
            'total_rental' :forms.NumberInput(attrs={'class' : 'form-control', 'id':'total_rental'}),
            'status' : forms.Select(attrs={'class' : 'form-control'}),
            'Category' : forms.Select(attrs={'class' : 'form-control'}),
        }