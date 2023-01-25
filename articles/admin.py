from django.contrib import admin

from .models import Article
from django.core.exceptions import ValidationError
from .models import Article, ArticleSection, Section
from django.forms import BaseInlineFormSet


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [ArticleSectionInLine]

class ArticleSectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        flag = 0
        for form in self.forms:

            if form.cleaned_data.get('DELETE'):
                continue

            if form.cleaned_data.get('is_main'):
                flag += 1

            if flag > 1:
                raise ValidationError('Выберите 1 основной раздел.')

        if flag == 0:
            raise ValidationError('Выберите 1 основной раздел.')
        return super().clean()


class ArticleSectionInLine(admin.TabularInline):
    model = ArticleSection
    extra = 2
    formset = ArticleSectionInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleSectionInLine]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name']
