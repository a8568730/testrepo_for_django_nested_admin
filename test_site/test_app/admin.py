from django.contrib import admin
import nested_admin

from test_app.models import HeadWord, Pronunciation


class PronunciationInline(
    #     InlineOrderMixin,
    nested_admin.SortableHiddenMixin,
    nested_admin.NestedTabularInline,
):
    model = Pronunciation
    fields = ('pronunce', 'order', )
    sortable_field_name = 'order'


class HeadWordAdmin(nested_admin.NestedModelAdmin):
    list_display = ('id', 'word',)
    inlines = [PronunciationInline, ]


admin.site.register(HeadWord, HeadWordAdmin)
admin.site.register(Pronunciation)
