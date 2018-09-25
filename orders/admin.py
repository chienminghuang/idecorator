from django.contrib import admin
from .models import 產品列表
# Register your models here.


#admin.site.register(產品列表)

#class 商品類別表Admin(admin.ModelAdmin):
#    list_display = ['id','名稱','圖片']

#admin.site.register(商品類別表,商品類別表Admin)




class  產品列表Admin(admin.ModelAdmin):
    list_display = ['id', '名稱','圖片','價格', '已上架', '建立時間', '修改時間']
    list_editable = ['名稱','價格', '已上架' ]
    list_per_page = 10

admin.site.register(產品列表,產品列表Admin)