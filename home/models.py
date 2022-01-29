from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10,null = True,blank=True)
    email = models.EmailField(max_length=150,null = True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null = True,blank=True)

    def __str__(self):
        return self.user_name




class Category(models.Model):
    name = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add= True,null = True,blank=True)

    def __str__(self):
        return self.name




class Book(models.Model):
    name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete= models.CASCADE,related_name="book_list")
    publish_date = models.DateField(auto_now_add= False )
    price = models.DecimalField( max_digits=5, decimal_places=2)
    created_date = models.DateField(auto_now_add=False ,null = True,blank=True)

    def __str__(self):
        return self.name




class Order(models.Model):
    ordered_by = models.ForeignKey(User,on_delete = models.CASCADE,related_name="order")
    book = models.ManyToManyField(Book)
    ordered_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.ordered_by)

    def get_books(self):
        return "\n".join([p for p in self.book.all()])    


