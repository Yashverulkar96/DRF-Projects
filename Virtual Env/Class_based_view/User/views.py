from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework import generics
from .models import Users
from .serializers import UserSerializer



# Create your views here.
# Class based view APIVIEW-----------------------------------------
class User(APIView):

    # List of all user
    def get(self, request, format=None):
        user= Users.objects.all()
        serializer=UserSerializer(user, many=True)
        return Response(serializer.data)
    
    #Create user  
    def post(self, request, format=None):
        serializer= UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class User_details(APIView):

    # get single object
    def get_user(self, pk):
        try:
            return Users.objects.get(pk=pk) 
        except Users.DoesNotExist:
            return Response({"msg":"Data not found"},status= status.HTTP_404_NOT_FOUND)
        
    def get(self,request,pk, format=None):
        user=self.get_user(pk)
        serializer=UserSerializer(user)
        return Response(serializer.data)
        
    
    def put(self, request, pk, format=None):
        user=self.get_user(pk)
        serializer=UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user=self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------

# using Generic view
# class User(generics.ListCreateAPIView):
#     queryset = Users.objects.all()
#     serilizer_class=UserSerializer

# class User_details(generics.RetrieveUpdateDestroyAPIView):
#     queryset =Users.objects.all()
#     serializer_class=UserSerializer


    