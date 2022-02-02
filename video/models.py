from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from cloudinary.models import CloudinaryField
from djrichtextfield.models import RichTextField
# Create your models here.


class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = CloudinaryField(resource_type='')
    description = RichTextField()
    date_published = models.DateTimeField(auto_now_add=True,
                                          verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True,
                                        verbose_name="date updated")

    def __str__(self):
        return self.caption


@receiver(post_delete, sender=Video)
def submission_delet(sender, instance, **kwargs):
    instance.video.delete(False)
