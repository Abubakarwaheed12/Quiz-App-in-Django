from django.urls import path
from quiz.views import home , get_quiz , quiz
urlpatterns=[
    path('' , home , name='home'),
    path('api/getquiz/' , get_quiz),
    path('quiz/' , quiz),
]