from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
# Create your models here.

class Post(models.Model):
    title= models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(blank=True,null=True)
    content = models.TextField(_("Content"))


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE) 
    username = models.CharField(_("Username"), max_length=150)
    content = models.TextField(_("Content"))
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    

    class Meta:
        ordering = ['-created']

CHOICES = (
    (1,'Male'),
    (2,'Female')
)


class Shepp(models.Model):
    name = models.CharField(max_length=255)
    male = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return self.name


@receiver(pre_save,sender=Post)
def my_callback(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)