from django.db import models


# Create your models here.
class Post(models.Model):
    titlu = models.CharField(max_length=255)
    slug = models.SlugField()
    git_link = models.TextField(null=True, blank=True)
    descriere = models.TextField()
    imagine = models.ImageField(null=True, blank=True)
    imagine_post1 = models.ImageField(null=True, blank=True)
    imagine_post2 = models.ImageField(null=True, blank=True)
    imagine_post3 = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titlu

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

