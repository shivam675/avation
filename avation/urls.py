"""avation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from micro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('setprofile/', views.set_user_profile, name = 'setprofile'),
    path('aboutus', views.aboutus, name = 'aboutus' ),
    path("contact/", views.ContactCreate, name="contact"),
    path("thanks/", views.thanks, name="thanks"),


    # uav all urls
    path('uavs/', include('uav.urls'), name='uavs'),

    # all FixedWing
    path('fixedwing/', include('fixedwing.urls'), name='fixedwing'),

    # All training
    path('training/', include('training.urls'), name='training'),

    # All multirotor
    path('multirotors/', include('multirotors.urls'), name='multirotors'),

    # all commercial
    path('commercial/', include('commercial.urls'), name='commercial'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
