"""webstrempreneur URL Configuration

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
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from Accounts import views as views_account
from webapp import views as views_webapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views_account.loginPage, name="login"),
    path('logout/', views_account.logoutUser, name="logout"),

    path('home/', views_webapp.home, name="home"),
]
