from django.apps import apps
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Category, Primarycategory, Secondarycategory
from .serializers import CategorySerializer, PrimarycategorySerializer, SecondarycategorySerializer


def get_id_from_title(title):
    queryset_categories = Category.objects.filter().order_by("id").values()
    for queryset_category in queryset_categories:
        print (queryset_category)
        if queryset_category['title'] == title:
            return queryset_category['id']
    return None


@api_view(['GET'])
@permission_classes((AllowAny,))
def categories(request):
    if request.method == 'GET':
        queryset = Category.objects.filter(visible=True).order_by("-created_at")
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "data not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def postCategory(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny,))
def getPrimaryCategory(request):
    if request.method == 'GET':
        queryset = Primarycategory.objects.filter(visible=True).order_by("title")
        serializer = PrimarycategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "data not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((AllowAny,))
def getPrimaryCategoryDetails(request, id):
    if request.method == 'GET':
        queryset_secondary = Secondarycategory.objects.filter(primary_category_id=id)
        # for secondary_data in queryset_secondary:
        #     secondary_title = secondary_data['title']
        #     secondary_id=secondary_data['id']
        #     print(secondary_data)
        #     queryset_category = Category.objects.filter(
        #         secondary_category_id=secondary_id).values()
        serializer = SecondarycategorySerializer(queryset_secondary, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "data not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes((AllowAny,))
def getCategoryDetails(request, id,sec_id):
    if request.method == 'GET':
        queryset_secondary = Secondarycategory.objects.filter(primary_category_id=id)
        queryset_secondary=queryset_secondary.objects.filter(pk=sec_id)
        if queryset_secondary:
            queryset_category=Category.objects.filter(secondary_category_id=sec_id)
        # for secondary_data in queryset_secondary:
        #     secondary_title = secondary_data['title']
        #     secondary_id=secondary_data['id']
        #     print(secondary_data)
        #     queryset_category = Category.objects.filter(
        #         secondary_category_id=secondary_id).values()
        serializer = CategorySerializer(queryset_category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "data not found"}, status=status.HTTP_404_NOT_FOUND)