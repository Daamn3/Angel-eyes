"""
URL configuration for main_project project.

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

from myapp import views

urlpatterns = [
    path('login_get/',views.login_get),
    path('login_post/',views.login_post),
    path('logout_all/',views.logout_all),
    path('index_get/',views.index_get),
    path('forgotpass_get/',views.forgotpass_get),
    path('send_reply_get/<id>',views.send_reply_get),
    path('view_blindperson_get/',views.view_blindperson_get),
    path('view_caretaker_get/',views.view_caretaker_get),
    path('view_complaint_get/',views.view_complaint_get),
    path('objects_manage_get/',views.objects_manage_get),
    path('view_object_get/',views.view_object_get),
    path('objects_manage_post/',views.objects_manage_post),
    path('edit_objects_get/<id>',views.edit_objects_get),
    path('edit_objects_post/',views.edit_objects_post),
    path('delete_object/<id>',views.delete_object),
    path('send_reply_post/',views.send_reply_post),
    path('ct_register/',views.ct_register),
    path('ct_home/',views.ct_home),
    path('pro_pic/',views.pro_pic),
    path('pro_det/',views.pro_det),
    path('Editprof/',views.Editprof),
    path('Editprof_post/',views.Editprof_post),
    path('viewbp/',views.viewbp),
    path('addbp/',views.addbp),
    path('editbp/',views.editbp),
    path('editbp_post/',views.editbp_post),

    path('delete_blind/',views.delete_blind),
    path('viewfp/',views.viewfp),
    path('addfp/',views.addfp),
    path('caretaker_view_blind_for_fami/',views.caretaker_view_blind_for_fami),




]
