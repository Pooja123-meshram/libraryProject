from django.contrib import admin
from .models import Author

class adminAuthor(admin.ModelAdmin):
    list_display=["name","email","bio"]
admin.site.register(Author,adminAuthor)
