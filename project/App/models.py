from django.db import models

class table_p(models.Model):
    Products = models.CharField(max_length=20)
    Quantity = models.IntegerField()

class table_l(models.Model):
    Location = models.CharField(max_length=20)

class table_t(models.Model):
    Timestamp = models.DateTimeField()
    Products = models.CharField(max_length=20)
    From_L = models.CharField(max_length=20)
    To_L = models.CharField(max_length=20)
    Quantity = models.IntegerField()



    
