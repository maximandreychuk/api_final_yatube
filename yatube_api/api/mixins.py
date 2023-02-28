from rest_framework import viewsets, mixins


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Вьюсет для подписок. Запросы только GET и POST."""
    pass
