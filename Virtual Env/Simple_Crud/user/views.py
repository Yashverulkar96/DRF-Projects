from rest_framework import viewsets 
from .models import User, Address
from .serializers import UserSerializer,AddressSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset=Address.objects.all()
    serializer_class=AddressSerializer