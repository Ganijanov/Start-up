from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.City)
admin.site.register(models.Helpless)
admin.site.register(models.HelplessMedia)
admin.site.register(models.Blog)
admin.site.register(models.BlogMedia)
admin.site.register(models.HelpType)