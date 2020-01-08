from django.db import models
from django.conf import settings

def upload_status_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class StatusQuerySet(models.QuerySet):
    pass

    # def serialize(self):
    #     list_values = list(self.values('user', 'content', 'image', 'id'))
    #     # print (list_values)
    #     return json.dumps(list_values)


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_status_image, blank=True, null=True)
    udpated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = StatusManager()

    def __str__(self):
        return str(self.content)[:50]


    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'