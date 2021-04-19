from django.contrib import admin
from .models import Contact
# Register your models here.



class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'number')
    fieldsets = ((None,{'fields': ('first_name','last_name','number','message')}),)
    search_fields = ('first_name',)
admin.site.register(Contact, ContactAdmin)
