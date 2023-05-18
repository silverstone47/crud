from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import User
from .serializers import UserSerializer


@csrf_exempt
def userApi(request, id=0):
    if request.method=='GET':
        user = User.objects.all()
        user_serializers = UserSerializer(user, many=True)
        return JsonResponse(user_serializers.data, safe=False)
    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        user_serializers = UserSerializer(data=user_data)
        if user_serializers.is_valid():
            user_serializers.save()
            return JsonResponse('Added', safe=False)
        return JsonResponse('not Added', safe=False)
    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(userId=user_data['userId'])
        user_serializers = UserSerializer(user, data=user_data)
        if user_serializers.is_valid():
            user_serializers.save()
            return JsonResponse('updated', safe=False)
        return JsonResponse('failed to update',safe=False)
    elif request.method=='DELETE':
        user = User.objects.get(userId=id)
        user.delete()
        return JsonResponse('deleted', safe=False)
    return JsonResponse('delete failed')            

