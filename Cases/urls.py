
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import results,homepage,caseslist,adminloginview,authenticateadmin,adminhomepage,logoutadmin

urlpatterns = [
    path('admin/', adminloginview,name='adminloginpage'),
    path('adminauthenticate/',authenticateadmin),
    path('adminhomepage/',adminhomepage,name='adminhomepage'),
    path('adminlogout/',logoutadmin),
    path('caselist/',caseslist,name='caselist'),
    path('',homepage),
    path('results/',results),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)