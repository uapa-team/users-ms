from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # new fields
        del token['user_id']

        token['username'] = user.username
        token['full_name'] = f'{user.first_name} {user.last_name}'
        token['groups'] = [group.name for group in user.groups.all()]
        token['permissions'] = list(user.get_all_permissions())

        return token

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer