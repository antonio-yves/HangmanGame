from django.contrib import admin

from . import models

admin.site.register(models.Word)
admin.site.register(models.Game)
admin.site.register(models.Score)

