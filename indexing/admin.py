from django.contrib import admin
from django import forms

from . import models
from ckeditor.widgets import CKEditorWidget

admin.site.register(models.Categories)
admin.site.register(models.Product)


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Police
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(models.Police, PostAdmin)


class TransportAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Transport
        fields = '__all__'


class TransportAdmin(admin.ModelAdmin):
    form = TransportAdminForm


admin.site.register(models.Transport, TransportAdmin)


class SalesAdmin(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Sale
        fields = '__all__'


class SalesAdmins(admin.ModelAdmin):
    form = TransportAdminForm


admin.site.register(models.Sale, SalesAdmins)
