from django import forms
from .models import Book
#DataFlair
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
        
        
        # https://github.com/Sumon-Rana/DJ_PROJECT.git