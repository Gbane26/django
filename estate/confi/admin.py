from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ConfigAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'logo1',
        'logo2',
        'adress',
        'lien_map',
        'cel',
        'phone',
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
        'logo1',
        'logo2',
        'adress',
        'lien_map',
        'cel',
        'phone',
        'description',
        'statut',
        'date_add',
        'date_upd',
    )


class SlideAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'image', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'image',
        'statut',
        'date_add',
        'date_upd',
    )


class AvenirAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'prix',
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
        'prix',
        'statut',
        'date_add',
        'date_upd',
    )


class Page_topAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'titre',
        'description',
        'image_back',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'titre',
        'description',
        'image_back',
        'statut',
        'date_add',
        'date_upd',
    )


class SociauxAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'icon', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'icon',
        'statut',
        'date_add',
        'date_upd',
    )


class AnonceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'icon',
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
        'icon',
        'statut',
        'date_add',
        'date_upd',
    )


class DemandeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'description',
        'contact',
        'image',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'description',
        'contact',
        'image',
        'statut',
        'date_add',
        'date_upd',
    )


class FooterAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'statut',
        'date_add',
        'date_upd',
    )


class Footer_detailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'footer',
        'titre',
        'lien',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'footer',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'footer',
        'titre',
        'lien',
        'statut',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Config, ConfigAdmin)
_register(models.Slide, SlideAdmin)
_register(models.Avenir, AvenirAdmin)
_register(models.Page_top, Page_topAdmin)
_register(models.Sociaux, SociauxAdmin)
_register(models.Anonce, AnonceAdmin)
_register(models.Demande, DemandeAdmin)
_register(models.Footer, FooterAdmin)
_register(models.Footer_detail, Footer_detailAdmin)
