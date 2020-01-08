from django.contrib import admin

from .models import Status as StatusModel
from .forms import StatusForm


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'image']
    form = StatusForm


admin.site.register(StatusModel, StatusAdmin)
