from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'model_building'

urlpatterns = [
    path('', views.all_modelling, name='all_modelling'),
    path('<int:post_id>/', views.detail, name='detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
