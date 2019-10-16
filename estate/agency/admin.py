from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class HouseAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categorie',
        'titre',
        'description',
        'position',
        'contenue',
        'prix',
        'image',
        'image_accueil',
        'isDisponible',
        'isSoldout',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'categorie',
        'isDisponible',
        'isSoldout',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'categorie',
        'titre',
        'description',
        'position',
        'contenue',
        'prix',
        'image',
        'image_accueil',
        'isDisponible',
        'isSoldout',
        'statut',
        'date_add',
        'date_upd',
    )


class LocationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'category',
        'titre',
        'image',
        'image_vue',
        'lien_video',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'category',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'category',
        'titre',
        'image',
        'image_vue',
        'lien_video',
        'statut',
        'date_add',
        'date_upd',
    )


class Info_houseAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'house',
        'titre',
        'icon',
        'noumbre',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'house',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'house',
        'titre',
        'icon',
        'noumbre',
        'statut',
        'date_add',
        'date_upd',
    )


class image_apercuAdmin(admin.ModelAdmin):

    list_display = ('id', 'house', 'image', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'house',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'house',
        'image',
        'statut',
        'date_add',
        'date_upd',
    )


class PresentationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'description',
        'statut',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.House, HouseAdmin)
_register(models.Location, LocationAdmin)
_register(models.Info_house, Info_houseAdmin)
_register(models.image_apercu, image_apercuAdmin)
_register(models.Presentation, PresentationAdmin)
