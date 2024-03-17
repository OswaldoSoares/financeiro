from django.contrib import admin
from transactions import models

admin.site.register(models.Companies)
admin.site.register(models.Categories)
admin.site.register(models.Registries)
admin.site.register(models.RegistryItens)
admin.site.register(models.Payments)
admin.site.register(models.Methods)
