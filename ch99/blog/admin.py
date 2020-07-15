from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    list_filter = ("modify_dt", )
    # 탐색기 기능
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title", )}

    # 태그 관련
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    # 태그관련
    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

