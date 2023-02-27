from posts.models import Post
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomPaginate(LimitOffsetPagination):

    def get_paginated_response(self, data):
        limit = self.request.query_params.get('limit')
        offset = self.request.query_params.get('offset')
        if limit is not None and offset is not None:
            return Response({
                "total posts": Post.objects.count(),
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'results': data
            })
        return Response(data)
