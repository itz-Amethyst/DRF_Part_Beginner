from API.models import Post
from django.http import Http404


def get_object(self, post_id):
    try:
        post = Post.objects.get(pk = post_id)
    except Post.DoesNotExist:
       raise Http404

    return post