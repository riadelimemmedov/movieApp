from django import forms
from django.forms import fields,widgets
from .models import *

class CommentForm(forms.ModelForm):#ModelForm yazilmasindaki sebeb Databaseni forma cevireciyik ele bil,sifirdan bir form yaratmayaciyig,eger sifirdan bir form yaratsag forms.Form olardi,amma hal hazirda forms.ModelForm yazilir
    class Meta:
        
        numbers = (#burda [] yazma hec baxt ic ice yaz ele bil tupleleari  amma list yazma choices de
            ('1','1 Yildiz'),
            ('2','2 Yildiz'),
            ('3','3 Yildiz'),
            ('4','4 Yildiz'),
            ('5','5 Yildiz'),
        )
        
        model = CommentMovie
        fields = '__all__'
        exclude = ['movie','date_comments']
        
        
        labels = {
            'full_name':'Ad Soyad',
            'your_email':'Eposta',
            'text':'Yorum',
            'rating':'Puan'
        },
        
        widgets = {
            'full_name': widgets.TextInput(attrs={'class':'form-control','placeholder':'Adiniz'}),
            'your_email': widgets.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'text':widgets.Textarea(attrs={'class':'form-control','placeholder':'Yorum'}),
            'rating':widgets.Select(attrs={'class':'form-control custom-select'},choices=numbers)
        }
        
        
        