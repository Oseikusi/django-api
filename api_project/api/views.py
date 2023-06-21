from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile

from .serializer import ProfileSerializer


# Create your views here.

@api_view(['GET','POST'])
def profile(request):
    if request.method == "GET":
        profile = Profile.objects.all()
        serializer= ProfileSerializer(profile, many=True)

        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
            
@api_view(['GET','PUT','DELETE'])
def profile_detail(request, id):
    try:
        profile = Profile.objects.get(pk=id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer= ProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method =="PUT":
        serializer = ProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
    elif request.method == "DELETE":
        profile.delete()
