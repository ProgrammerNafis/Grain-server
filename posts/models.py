from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    image_file = models.ImageField(upload_to='post_images/', blank=True, null=True)
    
    image_url = models.URLField(max_length=500, blank=True, null=True)
    
    
    
    @property
    def get_image(self):
        if self.image_file:
            return self.image_file.url
        elif self.image_url:
            return self.image_url
        return "https://via.placeholder.com/400"
        

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
        
        
        
        
        
#usr cmnt


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)
    admin_message = models.TextField(blank=True, help_text="Message from Admin to this User")

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE) # শুধু লগইন করা ইউজার
    body = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies') # রিপ্লাই সিস্টেম
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"By {this.user.username} on {this.post.title}"