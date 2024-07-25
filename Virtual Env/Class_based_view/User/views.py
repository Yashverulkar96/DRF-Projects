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
            return None
        
    def get(self,request,pk, format=None):
        user=self.get_user(pk)
        if user is not None:
            serializer=UserSerializer(user)
            return Response(serializer.data)
        else :
            return Response({"msg":"Data not found"},status= status.HTTP_404_NOT_FOUND)
        
    
    def put(self, request, pk, format=None):
        user=self.get_user(pk)
        if user is not None:
            serializer=UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
           return Response({"msg":"Data not avialable for update"},status= status.HTTP_404_NOT_FOUND) 
    
    def delete(self, request, pk, format=None):
        user=self.get_user(pk)
        if user is not None:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"msg":"Data not available to delete"},status= status.HTTP_404_NOT_FOUND) 

# ---------------------------------------------------------------------

# using Generic view
# class User(generics.ListCreateAPIView):
#     queryset = Users.objects.all()
#     serilizer_class=UserSerializer

# class User_details(generics.RetrieveUpdateDestroyAPIView):
#     queryset =Users.objects.all()
#     serializer_class=UserSerializer


    