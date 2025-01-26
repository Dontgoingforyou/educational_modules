from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from users.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """ Представление для управления пользователями. """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['username']
    ordering_fields = ['username']
    ordering = ['username']

    @action(detail=True, methods=['patch'], permission_classes=[IsAdminUser])
    def update_role(self, request, pk=None) -> Response:
        """ Обновляет роль пользователя. """

        user = self.get_object()
        new_role = request.data.get('role')

        if new_role not in dict(User.ROLE_CHOICES).keys():
            return Response({'error': 'Неправильная роль'}, status=status.HTTP_400_BAD_REQUEST)

        user.role = new_role
        user.save()

        return Response({'status': f'Роль пользователя обновлена до {user.get_role_display()}'})
