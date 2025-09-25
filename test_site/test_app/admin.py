from django.contrib import admin
import nested_admin

from test_app.models import HeadWord, Pronunciation, \
    CategoryMapping, Category


class PronunciationInline(
    nested_admin.SortableHiddenMixin,
    nested_admin.NestedTabularInline,
):
    model = Pronunciation
    fields = ('pronunce', 'order', )
    sortable_field_name = 'order'


class CategoryMappingInline(
    nested_admin.SortableHiddenMixin,
    nested_admin.NestedTabularInline,
):
    model = CategoryMapping
    fk_name = 'headword'
    classes = ['collapse']
    sortable_field_name = 'order'


class HeadWordAdmin(nested_admin.NestedModelAdmin):
    list_display = ('id', 'word',)
    inlines = [PronunciationInline, CategoryMappingInline, ]


admin.site.register(HeadWord, HeadWordAdmin)
admin.site.register(Category)
