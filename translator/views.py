from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer


# Base class to handle shared behavior
class BaseTranslationViewSet(APIView):
    """
    Base class for translation views to handle CRUD operations for specific language pairs.
    """
    source_languages = []
    target_languages = []

    def get_queryset(self):
        return Translation.objects.filter(
            source_language__in=self.source_languages,
            target_language__in=self.target_languages
        )

    def get(self, request):
        data = self.get_queryset()
        serializer = TranslationSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TranslationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        translation = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = TranslationSerializer(translation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        translation = get_object_or_404(self.get_queryset(), pk=pk)
        translation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Specific ViewSets for each pair of languages
class FrenchSpanishTranslationViewSet(BaseTranslationViewSet):
    source_languages = ['FR', 'ES']
    target_languages = ['FR', 'ES']


class FrenchEnglishTranslationViewSet(BaseTranslationViewSet):
    source_languages = ['FR', 'EN']
    target_languages = ['FR', 'EN']


class SpanishEnglishTranslationViewSet(BaseTranslationViewSet):
    source_languages = ['ES', 'EN']
    target_languages = ['ES', 'EN']


class SpanishFrenchTranslationViewSet(BaseTranslationViewSet):
    source_languages = ['ES', 'FR']
    target_languages = ['ES', 'FR']


class EnglishFrenchTranslationViewSet(BaseTranslationViewSet):
    source_languages = ['EN', 'FR']
    target_languages = ['EN', 'FR']


# Generic views for HTML templates
def index(request):
    return render(request, 'index.html', context={})


def navbar(request):
    return render(request, 'navbar.html', context={})


def contact(request):
    return render(request, 'contact.html', context={})


def all_translations_html(request):
    """
    Display all translations in an HTML view.
    """
    data = Translation.objects.all()
    return render(request, 'AllTranslation.html', context={'data': data})


def add_translation_html(request):
    """
    Render a form or page for adding a new translation.
    """
    return render(request, 'AddTranslation.html', context={})


# Global API endpoints
class AllTranslations(APIView):
    """
    API to retrieve all translations without language restrictions.
    """
    def get(self, request):
        data = Translation.objects.all()
        serializer = TranslationSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddTranslation(APIView):
    """
    API to add a single translation.
    """
    def post(self, request):
        serializer = TranslationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddTranslationWithJson(APIView):
    """
    API to add multiple translations at once using a JSON array.
    """
    def post(self, request):
        try:
            data = request.data
            if not isinstance(data, list):
                return Response({"error": "Expected a list of translations."}, status=status.HTTP_400_BAD_REQUEST)

            serializer = TranslationSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def index(request):
    return render(request, 'index.html', context={})

def navbar(request):
    return render(request, 'navbar.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})

def AllTranslationHtml(request):
    data = Translation.objects.all()
    return render(request, 'AllTranslation.html', context={'data': data})

def AddTranslationHtml(request):
    return render(request, 'AddTranslation.html', context={})

class AllTranslations(APIView):
    def get(self, request): 
        
        data = Translation.objects.all() # get all the data from the Translation table
        serializer_data = TranslationSerializer(data, many=True) # serialize the data
        return Response(serializer_data.data, status=status.HTTP_200_OK) # return the serialized data
    
    
class AddTranslation(APIView):
    def post(self, request):
        data = request.data
        serializer_data = TranslationSerializer(data=data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)