from django.urls import path
from . import views

#app_name = 'catalog'
urlpatterns = [
  path('', views.index, name='index'),
  path('students/', views.StudentListView.as_view(), name='students'),
  path('introduction_page/', views.introduction_page, name='introduction_page'),
  path('counting_principle/', views.counting_principle , name='counting_principle'),
  path('login/', views.login , name='login'),
  path('logout/', views.logout , name='logout'),
  path('personal_page/', views.personal_page , name='personal_page'),
  path('uploadFile/', views.uploadFile , name='uploadFile'),
  #path('ScoreBoard/', views.ScoreBoard, name='ScoreBoard'),
]