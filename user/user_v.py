from rest_framework import viewsets
from user.user_s import UserSerializer
from user.user_m import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_queryset(self):
    #     name = self.kwargs['name']
    #     return User.objects.filter(User__name = name)