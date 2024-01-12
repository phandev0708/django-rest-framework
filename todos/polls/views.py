from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer, GetAllQuestionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import timezone
from rest_framework.generics import get_object_or_404

# Create your views here.

class GetAllQuestion(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            return self.get_by_id(request, pk)
        list_question = Question.objects.all()
        mydata = GetAllQuestionSerializer(list_question, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

    def post(self, request):
        # print(request.data)
        mydata = QuestionSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Du lieu khong chinh xac', status=status.HTTP_400_BAD_REQUEST)
        title = mydata.data['question_text']
        time_pub = mydata.data['time_pub']
        question = Question.objects.create(question_text=title, time_pub=time_pub)
        return Response(data=question.id, status=status.HTTP_200_OK)

    def put(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        mydata = QuestionSerializer(instance=question, data=request.data)
        if not mydata.is_valid():
            return Response('Du lieu khong chinh xac', status=status.HTTP_400_BAD_REQUEST)
        mydata.save()
        return Response('Cap nhat thanh cong', status=status.HTTP_200_OK)

    def delete(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        question.delete()
        return Response('Xoa thanh cong', status=status.HTTP_204_NO_CONTENT)

    def get_by_id(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        mydata = QuestionSerializer(question)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

def index(request):
    myname = "Nguyễn Văn Phần"
    title = "Demo Django"
    items = ["Cấu trúc Django", "permission", "query", "filter", "serializer", "all"]
    context = {
        "name": myname,
        "title": title,
        "items": items
    }
    return render(request, "polls/index.html", context)

def viewQuestion(request):
    list_question = Question.objects.all()
    print(list_question[0].question_text)
    return HttpResponse("View Question " + list_question[0].question_text + "\n" + list_question[1].question_text )