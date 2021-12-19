from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.forms import fields, widgets
from .models import *
import random


class LoginForm(forms.Form):#Form yazilanda sifirdan bir form yaradilir
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control form-control-user',
        'placeholder':'Enter Email Address'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control form-control-user',
        'placeholder':'Enter Password'
    }))
    
    remember_me = forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'class':'custom-control-input',
    }))
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if not(User.objects.filter(email=email).exists()):#fyeni bele bir mail yoxdursa User objecttinde yoxdursa yeni not qoy basina ve ya ! isaresi
            self.add_error('email','Email or Password False')#birinci parametredeki email alani onu bildirirki,yeni yazdigimiz yeni elave ettdimiz self.add_error elave etsin errorsu formdaki email alanina yalniz,2 parametr ise errorun text dini gosterir
        return email

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name']#password1 ve password 2 alanlari,UserCreation form icinde var
        
        #eger deyisiklikler etmek isteyirsikse bu alanlarda yeni css baximindan ve ya basda cur def __init__(self,*args,**kwargs) dan istifade olunur

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #Burda self beraberdri UserCrationFormdan toreyen nesneler yeni inputlar
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'Password'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'Password Again'})
        self.fields['first_name'].widget = widgets.TextInput(attrs={'class':'form-control form-control-user','placeholder':'First Name'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Last Name'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class':'form-control form-control-user','placeholder':'Email'})
        
        #Yeni mecburidir deyer girmelisen
        self.fields['email'].required = True#yeni fieldslerden email alanini sec required ozelliyine True ver 
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if(User.objects.filter(email=email).exists()):
            self.add_error('email','Email Mevcut')
        return email
    
    def save(self,commit=True):#defaultda Truedur cunki
        user = super(UserCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1')) 
        user.username = "{}_{}_{}".format(
            self.cleaned_data.get('first_name').replace('ı','i').replace('ö','o').lower(),
            self.cleaned_data.get('last_name').lower(),
            random.randint(111,999)
        )
    
        if commit:
            user.save()
            
        return user
    
class UserPasswordChange(PasswordChangeForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)#Base classdan tore yeni
        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class':'form-control','placeholder':'Old Password'})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class':'form-control','placeholder':'Repeat New Password'})




class UserForm(forms.ModelForm):#yeni modelden miras alib rowlari formda istifade ede bilirsen forms.ModelForm sayesinde
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)#miras al User modeli
        self.fields['first_name'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'First Name'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'Last Name'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class':'form-control','placeholder':'Email'})
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Auth
        fields = ['avatar','location']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['location'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'Location'})
        
    