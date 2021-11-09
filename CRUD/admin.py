from django.contrib import admin

# Register your models here.
from CRUD.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Quote,QuoteAdmin)
