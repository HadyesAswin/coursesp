"""courses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('1',views.pyhome),
    path('2',views.pythonreg),
    path('3',views.python_registration),
    path('4',views.pythonpay),
    path('5',views.flutterhm),
    path('6',views.flutterreg),
    path('7',views.flutterpay),
    path('8',views.javahm),
    path('9',views.javareg),
    path('10',views.javapay),
    path('11',views.sqlhm),
    path('12',views.sqlreg),
    path('13',views.sqlpay),
    path('14',views.flutter_registration),
    path('15',views.java_registration),
    path('16',views.sql_registration),
    path('17',views.python_pay),
    path('18',views.flutter_pay),
    path('19',views.java_pay),
    path('20',views.sql_pay),



]
