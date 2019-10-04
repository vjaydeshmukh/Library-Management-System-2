from django.contrib import admin

from . import models

admin.site.register(models.Document)
admin.site.register(models.DocumentType)
admin.site.register(models.Author)
admin.site.register(models.Translator)
admin.site.register(models.Language)
admin.site.register(models.Publication)
admin.site.register(models.AgeClassification)
admin.site.register(models.Building)
admin.site.register(models.Comment)
admin.site.register(models.Location)
admin.site.register(models.Floor)