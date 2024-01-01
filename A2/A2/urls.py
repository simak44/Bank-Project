"""
URL configuration for A2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from banks import views
from branch import views as vw
from registration import views as vi
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.MyHomeView.as_view(), name='myhome'),
    path('usercreation/', vi.CreationFormView.as_view(), name='usercreation'),
    path('passreset/', vi.PassResetView.as_view(), name='passreset'),
    path('admin/', admin.site.urls),
    path('home/', login_required(views.HomeView.as_view()), name='home'),
    path('dashboard/', login_required(views.DashboardView.as_view()), name='dashboard'),
    

    path('branch/', include('branch.urls')),
    path('banks/', include('banks.urls'))


   



]
