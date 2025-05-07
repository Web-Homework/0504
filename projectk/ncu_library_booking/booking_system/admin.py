from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import KStudyArea, Seat # 從當前目錄的 models.py 匯入我們的模型

# 註冊 KStudyArea 模型到 Admin
admin.site.register(KStudyArea)

# 註冊 Seat 模型到 Admin
admin.site.register(Seat)

# 你也可以使用 @admin.register() 裝飾器的方式，效果一樣
# @admin.register(KStudyArea)
# class KStudyAreaAdmin(admin.ModelAdmin):
#     pass # 之後可以在這裡自訂 Admin 介面的顯示方式

# @admin.register(Seat)
# class SeatAdmin(admin.ModelAdmin):
#     pass # 之後可以在這裡自訂 Admin 介面的顯示方式