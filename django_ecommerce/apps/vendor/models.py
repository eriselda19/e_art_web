from django.contrib.auth.models import User
from django.db import models




class Vendor(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=254)
    profile_image=models.ImageField(upload_to='uploads/artisan/', blank=True, null=True)
    field=models.CharField(max_length=30, default='Artizan')
    #want this field to be populated automatically
    created_at=models.DateTimeField(auto_now_add=True)
    description=models.TextField(blank=True, null=True)
    #the relationship of the vendor and the user is one vendor on user
    #Cascade so when deleting a user we delete also the vendor
    created_by=models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)

    

    #returns a list ordered by name
    class Meta:
        ordering=['name']

    #this is a string representation of the object
    def __str__(self):
        return self.name

    


    def get_balance(self):
        items=self.items.filter(vendor_paid=False, order__vendors__in=[self.id])

        return sum((item.product.price * item.quantity) for item in items)

    def get_paid_amount(self):
        items=self.items.filter(vendor_paid=True, order__vendors__in=[self.id])

        return sum((item.product.price * item.quantity) for item in items)
