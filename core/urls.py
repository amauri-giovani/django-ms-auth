"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from two_factor.urls import urlpatterns as tf_urls

from customers.views import home, painel_seguro, dashboard, CustomLoginView

'''
path('', include(tf_urls)) adiciona rotas automáticas como:

/account/login/ com MFA
/account/setup/ para configurar o QR code
/account/logout/ e mais
'''

urlpatterns = [
    path('account/login/', CustomLoginView.as_view(), name='two_factor:login'),
    path('', include(tf_urls)),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('painel/', painel_seguro, name='painel_seguro'),
    path('dashboard/', dashboard, name='dashboard'),
]
