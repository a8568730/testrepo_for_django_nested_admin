from django.contrib import admin
from test_app.models import HeadWord, Pronunciation

# Register your models here.
admin.site.register(HeadWord)
admin.site.register(Pronunciation)


# class 主音讀Inline(
#     InlineOrderMixin,
#     nested_admin.SortableHiddenMixin,
#     nested_admin.NestedTabularInline,
# ):
#     model = 主音讀
#     fields = ('羅馬字', '第二優勢音', '音檔所在', '音檔發音人', '先後', )
#     extra = 0
#     max_num = 2
#     sortable_field_name = '先後'


# class SuTiauAdmin(nested_admin.NestedModelAdmin, CSSAdminMixin):
#     search_fields = ('id', '漢字', '主音讀__數字調', )  # for 近反義詞 auto complete
#     list_display = ('id', '漢字', '主羅馬字', '開放',)
#     list_display_links = ('id', '漢字', '主羅馬字')
#     ordering = ('-id',)
#     list_filter = (
#         '詞目類型',
#         '開放',
#         '警告',
#         sim_filter('初審'),
#         sim_filter('複審'),
#         sim_filter('定稿審'),
#     )
