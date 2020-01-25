from django.contrib import admin
from django.contrib.admin import ModelAdmin

from Adventures.models import Caracteristiques, Character, Competences, Ennemy, NPC, Physique, Equipement
from Adventures.models.Equipment import Outil, Armure, Arme, Bourse, Objet


class CaracteristiquesAdmin(ModelAdmin):
    exclude = ['']


class PhysiqueAdmin(ModelAdmin):
    exclude = ['']


class CompetencesAdmin(ModelAdmin):
    exclude = ['']


class EnnemyAdmin(ModelAdmin):
    exclude = ['']


class ArmureAdmin(ModelAdmin):
    exclude = ['']


class ArmeAdmin(ModelAdmin):
    exclude = ['']


class BourseAdmin(ModelAdmin):
    exclude = ['']


class ObjetAdmin(ModelAdmin):
    exclude = ['']


class OutilAdmin(ModelAdmin):
    exclude = ['']


class EquipementAdmin(ModelAdmin):
    exclude = ['']


class CharacterAdmin(ModelAdmin):
    exclude = ['']


class NPCAdmin(ModelAdmin):
    exclude = ['']


admin.site.register(Caracteristiques, CaracteristiquesAdmin)
admin.site.register(Physique, PhysiqueAdmin)
admin.site.register(Competences, CompetencesAdmin)
admin.site.register(Ennemy, EnnemyAdmin)
admin.site.register(Armure, ArmureAdmin)
admin.site.register(Arme, ArmeAdmin)
admin.site.register(Bourse, BourseAdmin)
admin.site.register(Objet, ObjetAdmin)
admin.site.register(Outil, OutilAdmin)
admin.site.register(Equipement, EquipementAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(NPC, NPCAdmin)
