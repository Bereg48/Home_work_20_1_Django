from django.conf import settings
from django.core.cache import cache

from main.models import Category


def get_cached_subject_for_category():
    if settings.CACHES_ENABLED:
        subject_list = cache.get('subject_list')
        if subject_list is None:
            subject_list = Category.objects.all()
            cache.set('subject_list', subject_list)
    else:
        subject_list = Category.objects.all()
        return subject_list