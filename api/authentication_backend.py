from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):

    def get_user(self, user_id):
            user = get_user_model().objects.filter(id=user_id).first()
            if not user :
                return None
            return user

    def authenticate(self, request, username=None, password=None):
            user = get_user_model().objects.filter(email=username).first()
            if user:
                if  user.check_password(password):
                    return user
            return None