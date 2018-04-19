from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display=['name','nickname','password','sex','email','image','create_time','update_time']
    list_per_page=2
    list_filter=['name']
    search_fields=['name']
admin.site.register(User,UserAdmin)

# Register your models here.
