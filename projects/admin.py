from django.contrib import admin

# Register your models here.
from .models import Project, Division, Tag

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)
    fieldsets = ((None,{'fields': ('title','description','image','url')}),)
    search_fields = ('title', 'url', 'description')

admin.site.register(Project, ProjectAdmin)








class ProjectTagAdmin(admin.StackedInline):
    model = Tag
    extra = 1

@admin.register(Division)
class ProjectDivisionAdmin(admin.ModelAdmin):
    inlines = [
    ProjectTagAdmin,
    ]
    class Meta:
        model = Division
