from django import forms
from .models import book

class bookf(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'
        labels = {'bi' : 'BOOK ID ' , 'bn'  : 'BOOK NAME ' , 'an' : 'AUTHOR NAME' , 'sn' : 'SHELF NO '}
        widgets = {
            'bi' : forms.TextInput(attrs={'class':'form-control'}),
            'bn' : forms.TextInput(attrs={'class':'form-control'}),
            'an' : forms.TextInput(attrs={'class':'form-control'}),
            'sn' : forms.TextInput(attrs={'class':'form-control'}),
            

        }