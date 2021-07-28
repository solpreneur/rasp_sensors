"""sensors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import htc.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', htc.views.dashboard),
    path('index', htc.views.dashboard, name='index'),
    path('login/', htc.views.login_view, name='login'),
    path('logout/', htc.views.logout_view, name='logout'),
    path('dashboard/', htc.views.dashboard, name='dashboard'),
   
    #get last known reading for the day
    path('reading/<reading_type>', htc.views.reading),
    path('reading/<reading_type>/', htc.views.reading),
   
   #get all data for the day i.e from when sensor started collecting data uptill when it Stopped
    path('read-day/<reading_type>', htc.views.read_day),
    path('read-day/<reading_type>/', htc.views.read_day),

  
    path('readings/', htc.views.readings, name='readings'),
]


urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)