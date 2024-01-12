from rest_framework import serializers
from .models import Question, Choice

class GetAllQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'time_pub')

class QuestionSerializer(serializers.Serializer):
    question_text = serializers.CharField(max_length=200)
    time_pub = serializers.DateTimeField()

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'vote')