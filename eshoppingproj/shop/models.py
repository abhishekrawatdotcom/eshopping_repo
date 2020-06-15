from django.db import models


# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    prii = models.IntegerField(default=0)
    desce = models.CharField(max_length=500, default='')
    desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/image', default="")

    def __str__(self):
        return self.product_name


class contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name

class orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=500)
    state=models.CharField(max_length=500)
    zip=models.IntegerField()
    phone=models.IntegerField()



class orderupdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=500)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:8] + "..."



class EMPMODEL(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=59)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)



