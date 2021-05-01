from django.contrib import admin

# Register your models here.
from .models import Commercial, CommercialImages, CommercialVideo, LearnPoints

class CommercialImagesAdmin(admin.StackedInline):
    model = CommercialImages
    extra = 1



class CommercialVideoAdmin(admin.StackedInline):
    model = CommercialVideo
    extra = 1

class LearnPointsCommertialAdmin(admin.StackedInline):
    model = LearnPoints
    extra = 1


# @admin.register(UavPost)
class CommercialAdmin(admin.ModelAdmin):
    inlines = [
    LearnPointsCommertialAdmin,
    CommercialImagesAdmin,
    CommercialVideoAdmin, 
    ]
    
    list_display = ('kind','date','image')
    fieldsets = ((None,{'fields': (
    'kind',
    'card_description',
    'image',
    'date',
    'brief_info',
    )}),)
    search_fields = ('title', 'date')
    class Meta:
        model = Commercial

admin.site.register(Commercial, CommercialAdmin)

