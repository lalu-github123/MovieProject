from django.urls import path
from . import views
app_name='webapp2'


urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add_movie,name='add'),
    path('movie/<int:id>/',views.detail,name='detail'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
