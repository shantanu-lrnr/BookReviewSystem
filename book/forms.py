from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['average_rating','created_at','updated_at']

        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter book title'
            }),

            'author':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter author name'
            }),

            'author_info' : forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a valid URL'
            }),

            'image':forms.ClearableFileInput(attrs={
                'class':'form-control',
            }),

            'description':forms.Textarea(attrs={
                'class':'form-control',
                'rows': 4,
                'placeholder':'Enter book description'
            }),

            'genre':forms.Select(attrs={
                'class':'form-control',
            }),

            'isbn':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter ISBN'
            }),

            'publication_date':forms.DateInput(attrs={
                'class':'form-control',
                'type':'date'
            }),

        }