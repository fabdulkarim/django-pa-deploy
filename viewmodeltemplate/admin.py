from django.contrib import admin

# Register your models here.

from .models import Blog, Mentee, Mentor

admin.site.register(Blog)
admin.site.register(Mentee)
admin.site.register(Mentor)