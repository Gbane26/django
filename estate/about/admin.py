from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class AboutAdmin(admin.ModelAdmin):

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


class AgendaAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'number',
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
        'number',
        'statut',
        'date_add',
        'date_upd',
    )


class About_imageAdmin(admin.ModelAdmin):

    list_display = ('id', 'image', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'image',
        'statut',
        'date_add',
        'date_upd',
    )


class TeamAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'fontion', 'description', 'image')
    list_filter = ('id', 'nom', 'fontion', 'description', 'image')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.About, AboutAdmin)
_register(models.Agenda, AgendaAdmin)
_register(models.About_image, About_imageAdmin)
_register(models.Team, TeamAdmin)
