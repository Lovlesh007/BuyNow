from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    

    class Meta:
        ordering = ('name',)
        
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
                        
        
class Product(models.Model):
    category = models.ForeignKey(Category,related_name="products")
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True,max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock =models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
