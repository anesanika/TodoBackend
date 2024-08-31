from rest_framework import viewsets, generics, views
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserRegistrationSerializer, UserSerializer
from rest_framework import permissions, response, exceptions
from rest_framework_simplejwt.tokens import RefreshToken

class UserView(views.APIView):
  permission_classes = (permissions.IsAuthenticated, )

  def get(self, request):
    serializer = UserSerializer(request.user)
    return response.Response(serializer.data)


class TaskViewSet(viewsets.ModelViewSet):
  permission_classes = (permissions.IsAuthenticated, )
  queryset = Task.objects.all()
  serializer_class = TaskSerializer

  def get_queryset(self):
    return Task.objects.filter(user=self.request.user)


class LoginViews(generics.GenericAPIView):
  permission_classes = [permissions.AllowAny,]
  
  def post(self, request, *args, **kwargs):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
      return response.Response({'detail': 'Username and password are required.'}, status=400)    

    user = authenticate(username=username, password=password)

    if user is None:
      raise exceptions.AuthenticationFailed("Invalid username or password.")

    refresh = RefreshToken.for_user(user)
    
    return response.Response ({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
    })
  

class RegsiterViews(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserRegistrationSerializer
  permission_classes = [permissions.AllowAny]
  