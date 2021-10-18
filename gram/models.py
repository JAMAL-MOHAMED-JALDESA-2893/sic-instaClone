from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.urls import reverse 


# Create your models here.
class Image(models.Model):
    image= CloudinaryField('image')
    author= models.ForeignKey(Profile, on_delete=models.CASCADE)
    name= models.CharField(max_length=30)
    caption= models.TextField()
    comments = models.CharField(max_length=30,blank=True)
    likes=models.ManyToManyField(User, related_name='blog_posts')
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def total_likes(self):
        return self.likes.count()
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        self._do_update()
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
