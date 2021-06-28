from django.urls import path
from . import views

app_name = 'resume'
urlpatterns = [
    path('', views.my_main_view, name='main'),
    path('education/', views.my_education_view, name='education'),
    path('other/', views.my_skills_view, name='skills'),
]
