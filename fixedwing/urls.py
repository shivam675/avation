from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'fixedwing'

urlpatterns = [
    path('', views.all_fixedwing, name='all_fixedwing'),
    path('<int:post_id>/', views.detail, name='detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
