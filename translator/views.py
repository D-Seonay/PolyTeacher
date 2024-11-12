from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from translator.models import Translation
from translator.serializers import TranslationSerializer

# Create your views here.

class FrenchSpanishTranslationViewSet(APIView):

    def get(self, request):
        # Filtrer les traductions où la langue source ou cible est le français ou l'espagnol
        data = Translation.objects.filter(
            source_language__in=['FR', 'ES'],
            target_language__in=['FR', 'ES']
        )
        serializer = TranslationSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TranslationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        translation = get_object_or_404(Translation, pk=pk)
        serializer = TranslationSerializer(translation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        translation = get_object_or_404(Translation, pk=pk)
        translation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class SpanishEnglishTranslationViewSet(APIView):
    
        def get(self, request):
            return Response(data={}, status=None)
        
        def post(self, request):
            return Response(data={}, status=None)
        
        def put(self, request, pk):
            return Response(data={}, status=None)
        
        def delete(self, request, pk):
            return Response(data={}, status=None)
        
class SpanishFrenchTranslationViewSet(APIView):
    
        def get(self, request):
            return Response(data={}, status=None)
        
        def post(self, request):
            return Response(data={}, status=None)
        
        def put(self, request, pk):
            return Response(data={}, status=None)
        
        def delete(self, request, pk):
            return Response(data={}, status=None)
        
class EnglishFrenchTranslationViewSet(APIView):
        
            def get(self, request):
                return Response(data={}, status=None)
            
            def post(self, request):
                return Response(data={}, status=None)
            
            def put(self, request, pk):
                return Response(data={}, status=None)
            
            def delete(self, request, pk):
                return Response(data={}, status=None)






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