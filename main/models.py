from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser


class KakaoUserManager(UserManager):

    def get_or_create_kakao_user(self, pk, extra_data):
        user = KakaoUser.objects.get(pk=pk)
        user.nickname = extra_data["kakao_account"]["profile"]["nickname"]
        user.profile_img = extra_data["kakao_account"]["profile"]["profile_image_url"]
        user.thumbnail_img = extra_data["kakao_account"]["profile"]["thumbnail_image_url"]
        user.save()
        return user


class KakaoUser(AbstractUser):
    nickname = models.CharField(max_length=30)
    profile_img = models.URLField()
    thumbnail_img = models.URLField()

    objects = KakaoUserManager()
