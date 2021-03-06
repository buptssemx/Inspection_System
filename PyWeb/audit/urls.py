from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('display/', views.display, name='display'),
    path('add/', views.add, name='add'),
    path('submit/', views.submit, name='submit'),
    path('download/', views.file_download, name='download'),
    path('dblist/', views.dblist, name='dblist'),
    path('upload', views.upload, name='upload'),
    path('review/<str:item_name>/', views.review, name='review'),
    path('<str:item_name>/', views.items, name='item_name'),

]
