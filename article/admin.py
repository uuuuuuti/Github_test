# -*- coding: utf-8 -*-

'''from django.contrib import admin
from django.contrib import admin 
from models import Article 
admin.site.register(Article)
'''

from django.contrib import admin
from models import Article
from pagedown.widgets import AdminPagedownWidget
from django import forms

# Register your models here.
# 定义自己的form
class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm


admin.site.register(Article,ArticleAdmin)

