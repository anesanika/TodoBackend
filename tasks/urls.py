from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, LoginViews, RegsiterViews, UserView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = [
  path('list/', include(router.urls)),
  path('login/', LoginViews.as_view(), name='login_page'),
  path('register/', RegsiterViews.as_view(), name='create_user_page'),
  path('me/', UserView.as_view(), name="user")
]
