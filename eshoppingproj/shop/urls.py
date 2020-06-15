from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index,name='shophome'),
    path('contact', views.contactview,name='shophome'),
    path('product/<int:myid>', views.productview,name='productview'),

    path('about', views.about,name='shophome'),
    path('checkout', views.checkout,name='shophome'),
    path('search', views.search,name='shophome'),
    path('handlerequest', views.handlerequest,name='shophome'),
    path('goto', views.pro1,name='shophome'),
    path('reg', views.registrationview,name='shophome'),
    path('log', views.loginview,name='shophome'),
    path('logout', views.logoutview,name='shophome'),
    path('loginhandle', views.loginhandle,name='shophome'),



]
