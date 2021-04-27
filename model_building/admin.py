from django.contrib import admin

# Register your models here.
from .models import ModelBulid, ModelImages, ModelVideo, LearnPoints

class ModelImagesAdmin(admin.StackedInline):
    model = ModelImages
    extra = 1



class ModelVideoAdmin(admin.StackedInline):
    model = ModelVideo
    extra = 1

class LearnPointsModelBuildAdmin(admin.StackedInline):
    model = LearnPoints
    extra = 1


# @admin.register(UavPost)
class ModelBulidAdmin(admin.ModelAdmin):
    inlines = [
    LearnPointsModelBuildAdmin,
    ModelImagesAdmin,
    ModelVideoAdmin, 
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
        model = ModelBulid

admin.site.register(ModelBulid, ModelBulidAdmin)

