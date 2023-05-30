from rest_framework.routers import DefaultRouter
from .views import QuizModeViewSet, QuestionModeViewSet, AnswerModeViewSet



router = DefaultRouter()


router.register('quiz', QuizModeViewSet)
router.register('question', QuestionModeViewSet)
router.register('answer', AnswerModeViewSet)

urlpatterns = router.urls
