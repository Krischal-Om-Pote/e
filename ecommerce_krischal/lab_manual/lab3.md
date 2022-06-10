OBJECTIVES:

1. Initializing the product_module.

2. Making different modules suitable as per needs and registering to database.
   INTRODUCTION:
   A model is the single, definitive source of information about data. It contains the essential fields and behaviors of the data that is being stored. Generally, each model maps to a single database table.

The basics:

Each model is a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.
With all of this, Django gives an automatically-generated database-access API
PROCEDURES:
In models.py, create a model for brands

code:
class Brand(models.Model):
name = models.CharField(max_length=200)
is_active = models.BooleanField()
Add the brand table to the database by python manage.py makemigartions and pyhton manage.py maigrate

In the 'admin.py', add the content at the admin panel using following code:

from.models import Brand
admin.site.register(Brand)
Run the server and verify the table by performing the CRUD operation.

     python manage.py runserver

In the 'model.py', edit the code for the brand model with following code:

class Brand(models.Model):
name = models.CharField(max_length=200)
is_active = models.BooleanField()
In the same file, edit the code for the category model

class Category(models.Model):
name = models.CharField(max_length=200)
is_active = models.BooleanField()
class Meta:
verbose_name_plural = "Categories"
Add the necessary fields to the product model

code:
class Product(models.Model):
name = models.CharField(max_length=200)
price = models.FloatField()
quantity = models.IntegerField()
image_url = models.CharField(max_length=500)
color_code = models.CharField(max_length=20)
brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
category = models.ForeignKey(Category, on_delete=models.CASCADE)
registered_on = models.DateTimeField()
is_active = models.BooleanField()
Save the changes to the database.

To enable the category and product models in the admin, add the following code:

from .models import Brand, Category, Product
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
Run the project server and verify the CRUD operations for brand, category and product respectively.

    python manage.py runserve

![](D:\ecommerce_project\ecommerce_krischal\ecommerce_krischal\output\Lab 4\1.png);
