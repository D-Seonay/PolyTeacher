"""
URL configuration for polyteacher project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from translator.views import index, contact, AllTranslationHtml, AddTranslationHtml, navbar
from translator.views import AllTranslations
from translator.views import AddTranslation
from translator.views import FrenchSpanishTranslationViewSet
from translator.views import FrenchEnglishTranslationViewSet
from translator.views import SpanishEnglishTranslationViewSet
from translator.views import SpanishFrenchTranslationViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('navbar', navbar),
    path('contact', contact),
    path('AllTranslationHtml', AllTranslationHtml),
    path('AddTranslationHtml', AddTranslationHtml),
    path('api/AllTranslations', AllTranslations.as_view(), name='AllTranslasion'),
    path('api/AddTranslation', AddTranslation.as_view(), name='AddTranslation'),
    path('api/french_spanish_translator', FrenchSpanishTranslationViewSet.as_view(), name='french_spanish_translator'),
    path('api/french_english_translator', FrenchEnglishTranslationViewSet.as_view(), name='french_english_translator'),
    path('api/spanish_english_translator', SpanishEnglishTranslationViewSet.as_view(), name='spanish_english_translator'),
    path('api/spanish_french_translator', SpanishFrenchTranslationViewSet.as_view(), name='spanish_french_translator'),
    
]
