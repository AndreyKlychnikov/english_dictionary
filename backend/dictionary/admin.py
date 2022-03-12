from dictionary.models import Source, Word
from django.contrib import admin


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass
