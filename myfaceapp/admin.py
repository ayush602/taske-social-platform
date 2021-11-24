from django.contrib import admin
from .models import Post, profilemodel, Register


# Register your models here.
@admin.register(Post)
class post(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(profilemodel)
class Profile(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(Register)
class post(admin.ModelAdmin):
    list_display = ('name','email','password','mobile_number')

