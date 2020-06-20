from django.urls import path
from . import views

urlpatterns = [
	path('api/ques/', views.question_list)
]
