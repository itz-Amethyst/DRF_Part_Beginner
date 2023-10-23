from API.models import Post
from django.http import Http404


def get_object(object_id, object):
    try:
        post = object.objects.get(pk = object_id)
    except object.DoesNotExist:
       raise Http404

    return post