from django.contrib import admin
from App.models import table_p,table_l,table_t

class sub_admin(admin.ModelAdmin):
    columns=['Products','Quantity']

class sub_admin1(admin.ModelAdmin):
    columns_1=['Location']

class sub_admin2(admin.ModelAdmin):
    columns2 =["Timestamp","Products","From_L","To_L","Quantity"]

admin.site.register(table_p,sub_admin)
admin.site.register(table_l,sub_admin1)
admin.site.register(table_t,sub_admin2)