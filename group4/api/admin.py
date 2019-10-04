from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'description',
        'image',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'description',
        'image',
        'status',
        'date_add',
        'date_upd',
    )


class SousCategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categorie',
        'nom',
        'description',
        'image',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'categorie',
        'status',
        'date_add',
        'date_upd',
        'id',
        'categorie',
        'nom',
        'description',
        'image',
        'status',
        'date_add',
        'date_upd',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'sousCategorie',
        'nom',
        'description',
        'image',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'sousCategorie',
        'status',
        'date_add',
        'date_upd',
        'id',
        'sousCategorie',
        'nom',
        'description',
        'image',
        'status',
        'date_add',
        'date_upd',
    )


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'article',
        'user',
        'description',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'article',
        'user',
        'status',
        'date_add',
        'date_upd',
        'id',
        'article',
        'user',
        'description',
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.SousCategorie, SousCategorieAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
