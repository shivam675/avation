from django.contrib import admin

# Register your models here.
from .models import Project, Division, Tag

admin.site.register(Project)

class ProjectTagAdmin(admin.StackedInline):
    model = Tag

@admin.register(Division)
class ProjectDivisionAdmin(admin.ModelAdmin):
    inlines = [
    ProjectTagAdmin,
    ]
    class Meta:
        model = Division
