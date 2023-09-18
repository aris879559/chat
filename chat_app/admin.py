from django.contrib import admin

# Register your models here.
from django.contrib import admin

admin.site.site_header = '大江狗管理后台'  # 设置header
admin.site.site_title = '大江狗管理后台'  # 设置title
admin.site.index_title = '大江狗管理后台'

from .models import Task

admin.site.register(Task)