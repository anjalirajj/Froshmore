from django.contrib import admin
from .models import hostel, user_querry

# Register your models here.
admin.site.register(user_querry)
admin.site.register(hostel)
