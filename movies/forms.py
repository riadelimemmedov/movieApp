from django import forms
from django.forms import fields,widgets
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        
        numbers = (
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
        
        
        