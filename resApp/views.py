from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from resApp.models import Users
from resApp.serializers import UserSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def users_list(request):
    if request.method == 'GET':
        users = Users.objects.all()

        name = request.GET.get('name', None)

        if name is not None:
            users = users.filter(name_icontains=name)

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def users_details(request, pk):
    try:
        users = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return JsonResponse({'message:': 'This user does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        users_serializer = UserSerializer(users)
        return JsonResponse(users_serializer.data)

    elif request.method == 'PUT':
        users_data = JSONParser().parse(request)
        users_serializer = UserSerializer(users, data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse({'message':'User Updated Successfully'}, status=status.HTTP_200_OK)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        users.delete()
        return JsonResponse({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
