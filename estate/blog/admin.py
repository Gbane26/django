from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'statut', 'date_add', 'date_update')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'title',
        'statut',
        'date_add',
        'date_update',
    )


class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'statut', 'date_add', 'date_update')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'title',
        'statut',
        'date_add',
        'date_update',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'description',
        'image',
        'video',
        'statut',
        'date_add',
        'date_update',
        'Category_id',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'Category_id',
        'id',
        'title',
        'description',
        'image',
        'video',
        'statut',
        'date_add',
        'date_update',
        'Category_id',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Tag, TagAdmin)
_register(models.Article, ArticleAdmin)
