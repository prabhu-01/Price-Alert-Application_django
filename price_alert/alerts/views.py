from rest_framework import generics, permissions
from .models import Alert
from .serializers import AlertSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.core.cache import cache

class CreateAlertView(generics.CreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DeleteAlertView(generics.DestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class ListAlertsView(generics.ListAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        cached_alerts = cache.get(f'alerts_{user.id}')
        if not cached_alerts:
            alerts = Alert.objects.filter(user=user)
            cache.set(f'alerts_{user.id}', alerts, timeout=300)  # Cache for 5 minutes
            return alerts
        return cached_alerts
