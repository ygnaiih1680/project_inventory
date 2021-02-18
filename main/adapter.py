from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from main.models import KakaoUser


class KakaoAccountAdapter(DefaultSocialAccountAdapter):

    def save_user(self, request, sociallogin, form=None):
        user = super(KakaoAccountAdapter, self).save_user(request, sociallogin, form)
        return KakaoUser.objects.get_or_create_kakao_user(user.pk, sociallogin.account.extra_data)
