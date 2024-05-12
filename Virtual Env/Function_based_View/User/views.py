from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User

# Create your views here.
@api_view(['GET','POST'])
def user(request):
    if request.method == 'GET':
        user= User.objects.all()
        serializer=UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method =='POST':
        serializer=UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','PATCH','DELETE'])
def user_details(request,pk):
    user = None
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"Error message": "User not found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer=UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH' or request.method == 'PUT':
        serializer=UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'PUT':
    #     serializer=UserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------------------------------
# @api_view(['GET'])
# def user(request):
#     users = User.objects.all()
#     serializer=UserSerializer(users, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_user(request):
#     serializer=UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data , status=201)
#     return Response(serializer.errors, status=400)

# @api_view(['GET','PUT','PATCH','DELETE'])
# def user_details(request,pk):
#     user=User.objects.get(pk=pk)
    
#     if request.method=='GET':
#         serializer=UserSerializer(user)
#         return Response(serializer.data)
    
#     elif request.method=='PUT':
#         serializer=UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
    
#     elif request.method=='PATCH':
#         serializer=UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
    
    
#     elif request.method=='DELETE':
#         user.delete()
#         return Response(status=204)