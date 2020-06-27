from django.urls import path
from . import views

urlpatterns = [
        path('', views.question_index, name='question_index'),
        path('ask-question', views.question_ask, name='question_ask'),
        path('giveAnswer/<int:pk>/<slug:s>', views.answer_index, name='answer_index'),
        path('api/ques/', views.question_list),
        path('api/ques/<int:pk>', views.get_put_question),
        path('api/answer/', views.answer_list)
    
]
