from rest_framework.viewsets import ModelViewSet

from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer

class QuizModeViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionModeViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerModeViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer