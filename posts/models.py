from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title




class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,unique=True,verbose_name="Tag Name")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Created At")
    def __str__(self):
        return self.name 
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="posts")
    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({'Read' if self.is_read else 'Unread'})"