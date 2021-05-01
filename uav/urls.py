from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'uav'

urlpatterns = [
    path('', views.all_uavs, name='all_uavs'),
    path('<int:post_id>/', views.detail, name='detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
