from django.urls import path
from . import views
from polls.views import GetAllQuestion

urlpatterns = [
    path("", views.index, name="index"),
    path("viewQuestion/", views.viewQuestion, name="viewQuestion"),
    path('question/', GetAllQuestion.as_view(), name='get_all_questions'),
    path('question/<int:pk>/', GetAllQuestion.as_view(), name='get_question_by_id'),
]