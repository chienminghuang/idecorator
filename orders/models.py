from django.db import models

# Create your models here.
class Order (models.Model):
    name = models.CharField(max_length=200);
    phone = models.CharField(max_length=20);
    address = models.TextField();
    delivery_date = models.DateField(blank=True);
    product_id = models.TextField();
    payment_option = models.CharField(max_length=50);
    amount = models.IntegerField();
    order_status = models.CharField(max_length=50);


#from django.db.models import ForeignKey
#class 商品類別表(models.Model):
#    名稱 = models.CharField(max_length=50,unique=True)
#    描述 = models.TextField()
#    圖片 = models.ImageField(upload_to='category', blank=True)

#    class Meta:
#        verbose_name_plural = "商品類別表"
#        db_table = '商品類別表'

#   def __str__(self):
#       return self.名稱




class 產品列表(models.Model):
    名稱 = models.CharField(max_length=100, unique=True)
    描述 = models.TextField(blank=True)
    圖片 = models.ImageField(upload_to='category', blank=True)
#    所屬類別 = models.ForeignKey(商品類別表, on_delete=models.CASCADE)
    價格 = models.DecimalField(max_digits=10, decimal_places=4)
    庫存 = models.IntegerField(default=0)
    已上架 = models.BooleanField(default=True)
    建立時間 = models.DateTimeField(auto_now_add=True)
    修改時間 = models.DateTimeField(auto_now_add=True)

    # Meta後台管理介面
    class Meta:
        verbose_name_plural = "產品列表"
        db_table = '產品列表'
        ordering = ('-建立時間',)
        def __str__(self):
            return self.名稱
