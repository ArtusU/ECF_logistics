from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Referrer


def referrer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='referrer')
        instance.groups.add(group)

        Referrer.objects.create(
                user=instance,
                name=instance.username,
                email=instance.email,
                )

post_save.connect(referrer_profile, sender=User)