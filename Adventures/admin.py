from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from Adventures.models import Caracteristiques, Character, Competences, Ennemy, Equipment, NPC, Physique
from Adventures.models.Equipment import Outils, Armure, Arme, Bouclier, Bourse, Objets


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


class BouclierAdmin(ModelAdmin):
    exclude = ['']


class BourseAdmin(ModelAdmin):
    exclude = ['']


class ObjetsAdmin(ModelAdmin):
    exclude = ['']


class OutilsAdmin(ModelAdmin):
    exclude = ['']


class EquipmentAdmin(ModelAdmin):
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
admin.site.register(Bouclier, BouclierAdmin)
admin.site.register(Bourse, BourseAdmin)
admin.site.register(Objets, ObjetsAdmin)
admin.site.register(Outils, OutilsAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(NPC, NPCAdmin)
