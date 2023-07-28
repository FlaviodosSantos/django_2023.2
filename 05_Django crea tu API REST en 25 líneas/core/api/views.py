from rest_framework.viewsets import ModelViewSet
from core.models import Post
from core.api.serializers import PostSerializer


class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
