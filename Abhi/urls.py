from django.urls import path,include
from Abhi import views

urlpatterns = [
    path('post/',views.save,name='save'),
    path('get_all/',views.get_all, name = 'xyz'),
    path('disvouch/<int:mob>',views.dis_vouch,name = 'dis_vouch'),
    path('get_vouch/',views.get_vouch,name = 'get_vouch'),
    path('mar_login/<int:mob>',views.marchant_login,name = 'marchant_login'),
    path('read_vouch/<int:mob>',views.Read_vouch,name = 'Read_vouch'), 
    # path('frontpage', views.frontpage, name='frontpage')
]