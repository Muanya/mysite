from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('form', views.forms, name='form'),
	path('form/sucess', views.success_message, name='form-success-view'),
	path('project', views.project_index, name="project_index"),
	path('project/<int:pkey>/', views.project_detail, name="project_detail"),
	path('faq/questions', views.question_index, name='question_index' )
]