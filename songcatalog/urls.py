from django.urls import path
from . import views

urlpatterns = [

]
urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.SongListView.as_view(), name='songs'),
]
