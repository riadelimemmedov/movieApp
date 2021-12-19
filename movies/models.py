from typing import Generic
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator,MaxLengthValidator
from ckeditor.fields import  RichTextField
# Create your models here.

#!Filmin Tipi
class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

#!Elaqe 
class Contact(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return self.address

#!Filmde ki KADRO lar
class Person(models.Model):
    
    cinsiyyet = [
        ('M','Erkek'),
        ('F','Kadin')
    ]
    
    isci_kadrosu = [
        ('1','Gorevli'),#yeni reqem geldikde key olarag reqem verdikde biz bize hemin reqeme uygun deyeri donderecek dictionary
        ('2','Oyuncu'),
        ('3','Yonetmen'),
        ('4','Senarist')
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.CharField(max_length=3000)
    image_name = models.CharField(max_length=50)#eger charField yazmisansa mutleq ve mutleq sekilde max_lenght yazmalisan
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1,choices=cinsiyyet,verbose_name='Cinsiyyet')
    duty_type = models.CharField(max_length=1,choices=isci_kadrosu,verbose_name='Gorev')#eger charField yazirsansa mutleq ve mutleq mecburidir yeniki max_lenght qoyasan
    contact = models.OneToOneField(Contact,on_delete=models.CASCADE,null=True,blank=True)
    
    @property#@property kimi yazanda funksiyani,funksiya ozunu deyisken kimi aparir,yeni yuxardaki first_name ve s kimi
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    full_name.fget.short_description = 'Ad Soyad'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.isci_kadrosu[int(self.duty_type)-1][1]})"
    
    #verbose_name ve ya verbose_name_plural ve s onlara oxsar metodlari admin panelden deyismek ucun Meta classi icinde qeyd et
    class Meta:
        verbose_name = 'Kisi'
        verbose_name_plural = 'Kisiler'
    
    
#!Film Haqqinda
class Movie(models.Model):
    title = models.CharField(max_length=255,verbose_name='Baslik')
    description = RichTextField()
    image_name = models.ImageField(upload_to='movies',verbose_name='Film On Resim')
    image_cover = models.ImageField(upload_to='movies',verbose_name='Film ArkaPlan Resmi')
    date = models.DateField(verbose_name='Zaman')#DateField yazilib ve icin bos buraxilarsa onda zamani ozumuz secmeliyik ve ya autor_now=True yaza bilerik ozumuzun vaxti secmeyi ucun
    slug = models.SlugField(unique=True,db_index=True)
    budget = models.DecimalField(max_digits=20,decimal_places=2,verbose_name='Butce')
    language = models.CharField(max_length=255,verbose_name='Dil')
    people = models.ManyToManyField(Person,verbose_name='Filmde Yer Alan Karakterler')
    genres = models.ManyToManyField(Genre,verbose_name='Film Tipi')
    is_active = models.BooleanField(default=False)#yeni yeni activ olan filmler butun filmler yeni,butun filmleri getirsin filtterden True donurse eger
    is_active_home = models.BooleanField(default=False)#burda ise home pagede gosterilen filmler yalniz
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

#!Slider
class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='movies')
    movie = models.ForeignKey(Movie,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return str(self.title)
    
#!Video
class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)#Burda models.URLField dende istifade ede bilersen
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)#Yeni bir movie silinde eger ona aid videoda silinsin
    
    def __str__(self):
        return self.title
    
#!Comment Movie
class CommentMovie(models.Model):
    full_name = models.CharField(max_length=100,verbose_name='Yorum Yapan')
    your_email = models.EmailField(verbose_name='Email',default='')
    text = models.TextField(max_length=500,verbose_name='Yorum')
    rating = models.PositiveBigIntegerField(null=True)#validators=[MinLengthValidator(1),MaxLengthValidator(5)]#
    date_comments = models.DateTimeField(auto_now_add=True,null=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='yorumlar')
    
    
    def __str__(self):
        return str(self.movie)
    
    class Meta:
        ordering = ['-date_comments']#ordering hemise modelde  yazilmalidir cunki databasede siralanir tersine modelde databaye bagli oldugu ucun class Meta icindeki ordering = ['-date_comments'] i models.py icinde yazmliyig mutleq
    