from django.contrib import admin
from .models import *
from django.contrib.admin import TabularInline
from django import forms
from ckeditor.widgets import CKEditorWidget


class MyInlineModelForm(forms.ModelForm):
    class Meta:
        model = BlogContent
        fields = '__all__'
        widgets = {
            'text_content': CKEditorWidget(),
        }


class QueryTabularParam(TabularInline):
    model = BlogContent
    form = MyInlineModelForm
    extra = 1


class DefineBlogContent(admin.ModelAdmin):
    inlines = [QueryTabularParam,]



admin.site.register(HomePageContent,DefineBlogContent)
