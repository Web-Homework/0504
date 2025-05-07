from django.db import models

# Create your models here.
class KStudyArea(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="區域名稱") # 例如: "總圖書館大K中", "人社分館小K中"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "K書中心區域"
        verbose_name_plural = verbose_name


class Seat(models.Model):
    # 座位編號，例如 "A01", "K1-01"。我們假設在同一個區域內，座位編號是唯一的。
    seat_number = models.CharField(max_length=20, verbose_name="座位編號")
    # 座位所屬區域，使用外鍵關聯到 KStudyArea 模型
    area = models.ForeignKey(KStudyArea, on_delete=models.CASCADE, verbose_name="所屬區域")
    # 其他座位屬性 (可以根據你的需求增減)
    description = models.TextField(blank=True, null=True, verbose_name="座位描述") # 允許空白或空值
    is_available_for_booking = models.BooleanField(default=True, verbose_name="是否開放預約")

    # 為了確保同一個區域內的座位編號是唯一的
    class Meta:
        unique_together = ('area', 'seat_number') # 同一個區域下的座位號碼必須唯一
        verbose_name = "座位"
        verbose_name_plural = verbose_name # 在 admin 後台顯示的名稱

    def __str__(self):
        # 這個方法定義了當我們打印一個 Seat 物件時，它會顯示什麼
        # 例如，在 Django Admin 後台，會顯示這個字串
        return f"{self.area.name} - {self.seat_number}"