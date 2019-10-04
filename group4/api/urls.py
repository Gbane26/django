"""group4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from .apiviews import CategorieViewSet, CommentaireViewSet, SousCategorieViewSet, ArticleViewSet


router = DefaultRouter()
router.register('categories', CategorieViewSet, base_name='Categories')
router.register('SousCategories', SousCategorieViewSet, base_name='SousC')
router.register('article', ArticleViewSet, base_name='articles')
router.register('commentaire', CommentaireViewSet, base_name='commentaire')

urlpatterns = [
    # ...
]

urlpatterns += router.urls
