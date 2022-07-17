from unittest import signals
from catalog.models import Book, UserProfile
from django.db.models.signals import pre_save, post_save

pre_save.connect(UserProfile.set_slug, sender=UserProfile)
post_save.connect(UserProfile.set_membership, sender=UserProfile)
pre_save.connect(Book.set_slug, sender=Book)
