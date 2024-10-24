from django.urls import path, include
from . import views 



app_name = 'methodist'
urlpatterns = [
    path('', views.home, name='home'),
    path('methodist/', views.methodist, name="methodist"),
    path('template/', views.template, name = "template"),
    path('post_detail/<int:pk', views.post_detail, name='post_detail'),
    path('category/', views.category, name='category'),
    path('staff_list/', views.staff_list, name='staff_list'),
    path('plot/', views.plot_view, name='plot_view'),
   
]