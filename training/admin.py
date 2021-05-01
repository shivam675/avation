from django.contrib import admin

# Register your models here.
from .models import Training, TrainingImages, TrainingVideo, LearnPoints

class TrainingImagesAdmin(admin.StackedInline):
    model = TrainingImages
    extra = 1



class TrainingVideoAdmin(admin.StackedInline):
    model = TrainingVideo
    extra = 1

class LearnPointsAdmin(admin.StackedInline):
    model = LearnPoints
    extra = 1


# @admin.register(UavPost)
class TrainingAdmin(admin.ModelAdmin):
    inlines = [
    LearnPointsAdmin,
    TrainingImagesAdmin,
    TrainingVideoAdmin, 
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
        model = Training

admin.site.register(Training, TrainingAdmin)

