from django.contrib import admin

# Register your models here.
from django.contrib import admin

admin.site.site_header = '大江狗管理后台'  # 设置header
admin.site.site_title = '大江狗管理后台'  # 设置title
admin.site.index_title = '大江狗管理后台'

from .models import Task, Status
from django.utils.html import format_html

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('colored_name', 'status_text')

    def colored_name(self, obj):
        color_code = 'black'
        if obj.status == Status.UNSTARTED:
            color_code = 'red'
        elif obj.status == Status.ONGOING:
            color_code = 'orange'
        elif obj.status == Status.FINISHED:
            color_code = 'green'
        return format_html('<span style="color: {};">{}</span>', color_code, obj.name)
    colored_name.short_description = '任务名称'

    def status_text(self, obj):
        return dict(Status.choices)[obj.status]
    status_text.short_description = '任务状态'




