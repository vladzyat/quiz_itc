from rest_framework.routers import DefaultRouter

from .views import QuizUserModelViewSet

router = DefaultRouter()

router.register('', QuizUserModelViewSet)


urlpatterns = router.urls


