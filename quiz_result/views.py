from rest_framework.viewsets import ModelViewSet

from .models import QuizUser
from .serializers import QuizUserSerializer, GetQuizUserSerializer


class QuizUserModelViewSet(ModelViewSet):
    queryset = QuizUser.objects.all()
    serializer_class = QuizUserSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetQuizUserSerializer
        return QuizUserSerializer


