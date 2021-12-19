from django.contrib import admin
from .models import *
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','is_active','is_active_home']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ['genres','language','is_active','is_active_home']
    search_fields = ['title','description']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name','gender','duty_type']
    list_filter = ['gender','duty_type']
    search_fields = ['first_name','last_name']
    

class CommentAdmin(admin.ModelAdmin):
    list_display = ['full_name','movie']
    list_filter = ['full_name','movie']
    search_fields = ['movie__title','text']

admin.site.register(Movie,MovieAdmin)#Birinci mutleq oz modelini yaz sonra ise admin.py de yazdigin ve bu modelee bagla olan classli qeyd ed yoxsa kod islemez cunki birici model oxunmalidir sonra ise admin paneline tetbiq olunmalidir deyisiklikler
admin.site.register(Person,PersonAdmin)

admin.site.register(Contact)
admin.site.register(Genre)
admin.site.register(Video)
admin.site.register(CommentMovie,CommentAdmin)
admin.site.register(Slider)