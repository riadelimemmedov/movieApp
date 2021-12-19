from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            #!Burda verilen email uygun username tapmaliyig mutleqkki giris edende email ilede girmek mumkun olsun
            
            #if (User.objects.filter(email=email).exists()):exists() ancag filter metodu ile isleyir yeni bir yigin databaseni filterleyib gonderilen sorguya nezeren bele bir deyerin olub olmamasini yoxlayir exists() true ve ya false deyer geri donur
            username = User.objects.get(email=email).username
            user = authenticate(request,username=username,password=password)
            
            if user is not None:#eger bele bir istifadeci varsa login ol
                login(request,user)
                if not remember_me:#eger false dursa yeni remember me if islesin
                    request.session.set_expiry(0)
                    request.session.modified = True#yeni bildirekk deyisiklik etmisik
                return redirect('index') 
            else:
                form.add_error(None,'Not Found User')
                return render(request,'account/login.html',{'form':form})#cunki xetalar defaltda formun ozune mexsusdur buna gorede formu geiye dondermek lazimdir mecbur
            
        else:
            return render(request,'account/login.html',{'form':form})
    form = LoginForm()
    return render(request,'account/login.html',{'form':form})

def registerView(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()#burda save edende forms.py daki save metodu isleyecek
            username = user.username
            password = form.cleaned_data.get('password1')
            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect('index')
        else:
            form.add_error(None,'Formu Eksizsiz Doldurun')#None vermemdeki sebeb form.add_errra butun input yerlerine aid olsun hemin xeta None verilerek
            return render(request,'account/register.html',{'form':form})

    #else ele buradir eger else yazsan program casag bilmeyecek hansi islesin    
    form = RegisterUserForm()
    return render(request,'account/register.html',{'form':form})

def logoutView(request):
    logout(request)
    return redirect('index')


################################################################################################
@login_required(login_url='login')
def profileView(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,files=request.FILES,instance=request.user.auth)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.add_message(request,messages.SUCCESS,'Profil Bilgileriniz Basarili Bir Sekilde Guncellendi')
            return redirect('profile')
        else:
            messages.add_message(request,messages.INFO,'Lutfen Bilgileriniz Kontrol Ediniz')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.auth)#yeni girisn eden istifadecinin profilini goster profil burda auth modelidir
    return render(request,'account/profile.html',{'user_form':user_form,'profile_form':profile_form})


def changePasswordView(request):
    if request.method == 'POST':
        form = UserPasswordChange(request.user,request.POST or None)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)#bura onemlidir,yeni upda elediyin formu gonder session yerineki cokkiesde deyissin
            messages.add_message(request,messages.SUCCESS,'Parola Basarili Bir Sekilde Degistirildi')
            return redirect('change_password')
        else:
            return render(request,'account/changepassword.html',{'form':form})
            
    form = UserPasswordChange(request.user)
    return render(request,'account/changepassword.html',{'form':form})


def watchView(request):
    context = {
        
    }
    return render(request,'account/watchlist.html',context)

