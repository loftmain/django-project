from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt')
    list_filter = ("modify_dt", )
    # 탐색기 기능
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title", )}

