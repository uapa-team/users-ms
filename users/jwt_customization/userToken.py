from django.contrib.auth.models import Permission
from django.db.models import Q
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from uapapp.models import Programa, UsuarioDependencia


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # new fields
        del token['user_id']

        token['username'] = user.username
        token['full_name'] = f'{user.first_name} {user.last_name}'
        token['groups'] = [group.name for group in user.groups.all()]

        permissions = Permission.objects.filter(
            Q(user=user) | Q(group__in=user.groups.all()))

        token['permissions'] = [(p.codename, p.name) for p in set(permissions)]

        uapapp_dependencias = [rel.dependencia for rel in UsuarioDependencia.objects.filter(user=user)]
        uapapp_programs = Programa.objects.filter(
            dependencia__in=uapapp_dependencias
        )

        token['uapapp'] = {
            'programs': [(p.codigo, 1 if p.tipo == 'pre' else 0, p.nombre) for p in uapapp_programs]
        }

        return token

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer