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
        ('1','Gorevli'),
        ('2','Oyuncu'),
        ('3','Yonetmen'),
        ('4','Senarist')
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.CharField(max_length=3000)
    image_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1,choices=cinsiyyet,verbose_name='Cinsiyyet')
    duty_type = models.CharField(max_length=1,choices=isci_kadrosu,verbose_name='Gorev')
    contact = models.OneToOneField(Contact,on_delete=models.CASCADE,null=True,blank=True)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    full_name.fget.short_description = 'Ad Soyad'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.isci_kadrosu[int(self.duty_type)-1][1]})"
    
    
    class Meta:
        verbose_name = 'Kisi'
        verbose_name_plural = 'Kisiler'
    
    
#!Film Haqqinda
class Movie(models.Model):
    title = models.CharField(max_length=255,verbose_name='Baslik')
    description = RichTextField()
    image_name = models.ImageField(upload_to='movies',verbose_name='Film On Resim')
    image_cover = models.ImageField(upload_to='movies',verbose_name='Film ArkaPlan Resmi')
    date = models.DateField(verbose_name='Zaman')
    slug = models.SlugField(unique=True,db_index=True)
    budget = models.DecimalField(max_digits=20,decimal_places=2,verbose_name='Butce')
    language = models.CharField(max_length=255,verbose_name='Dil')
    people = models.ManyToManyField(Person,verbose_name='Filmde Yer Alan Karakterler')
    genres = models.ManyToManyField(Genre,verbose_name='Film Tipi')
    is_active = models.BooleanField(default=False)
    is_active_home = models.BooleanField(default=False)
    
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
    url = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
#!Comment Movie
class CommentMovie(models.Model):
    full_name = models.CharField(max_length=100,verbose_name='Yorum Yapan')
    your_email = models.EmailField(verbose_name='Email',default='')
    text = models.TextField(max_length=500,verbose_name='Yorum')
    rating = models.PositiveBigIntegerField(null=True)
    date_comments = models.DateTimeField(auto_now_add=True,null=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='yorumlar')
    
    
    def __str__(self):
        return str(self.movie)
    
    class Meta:
        ordering = ['-date_comments']    