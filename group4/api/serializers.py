from rest_framework import serializers

from .models import Categorie, SousCategorie, Article, Commentaire

from drf_dynamic_fields import DynamicFieldsMixin


class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    article_commentaire = CommentaireSerializer(many=True, required=False)

    class Meta:
        model = Article
        fields = '__all__'


class SousCategorieSerializer(serializers.ModelSerializer):
    article_cat = ArticleSerializer(many=True, required=False)

    class Meta:
        model = SousCategorie
        fields = '__all__'

class CategorieSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    souscategories = SousCategorieSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Categorie
        # fields = ('id', 'nom', 'description', 'status')
        fields = '__all__'