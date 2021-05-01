from django.contrib import admin

# Register your models here.
from .models import FixedWingPost, FixedWingImages, FixedWingVideo, FixedWingComment

class FixedWingImagesAdmin(admin.StackedInline):
    model = FixedWingImages
    extra = 1

# class PostUavCommentAdmin(admin.StackedInline):
#     model = Comment
#     extra = 1

class FixedWingVideoAdmin(admin.StackedInline):
    model = FixedWingVideo
    extra = 1


# @admin.register(UavPost)
class FixedWingPostAdmin(admin.ModelAdmin):
    inlines = [FixedWingImagesAdmin,
    FixedWingVideoAdmin]
    list_display = ('title','date','image')
    fieldsets = ((None,{'fields': (
    'title',
    'description',
    'image',
    'date',
    'Rotor_type',
    'RF_frequecy',
    'unit',


    'wing_Span_in_mm',
    'wing_Area_in_mm2',
    'average_Chord_in_mm',
    'weight_in_grams',
    'cruise_Speed_in_mtr_per_s',
    'microcontroller',
    'inertial_Measurement_Unit',
    'RC_Receiver',
    'RC_Transmitter',
    'servos',
    'electronic_Speed_Contorller',
    'brushless_Motor',

    )}),)
    search_fields = ('title', 'user_name')
    class Meta:
        model = FixedWingPost

admin.site.register(FixedWingPost, FixedWingPostAdmin)


# @admin.register(UavImages)
# class PostUavImageAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Comment)
class FixedWingPostCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post','created_at' ,'content')
    fieldsets = ((None,{'fields': ('post','user','content',)}),)
    search_fields = ('user', 'post', 'content')

admin.site.register(FixedWingComment, FixedWingPostCommentAdmin)
