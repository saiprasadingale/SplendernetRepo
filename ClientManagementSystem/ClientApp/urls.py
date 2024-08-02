from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.AddClient,name='addurl'),
    path('show/',views.ShowClient,name='showurl'),
    path('update/<int:id>/',views.UpdateClient,name='updateurl'),
    path('delete/<int:id>/',views.DeleteClient,name='deleteurl'),
]
