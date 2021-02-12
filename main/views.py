from django.shortcuts import render, redirect
import requests as req
import json


def index(request):
    return render(request, 'index.html')

#
# def kakao_login(request):
#     rest_api_key = '53b461faa6a8ffe4446e19ecb44a6ef1'
#     redirect_uri = 'http://127.0.0.1:8000/kakao_auth_code'
#     api_host = f'https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={redirect_uri}&response_type=code'
#     return redirect(api_host)
#
#
# def kakao_auth_code(request):
#     code = request.GET["code"]
#     rest_api_key = '53b461faa6a8ffe4446e19ecb44a6ef1'
#     redirect_uri = 'http://127.0.0.1:8000/kakao_auth_code'
#     api_host = f'https://kauth.kakao.com/oauth/token?client_id={rest_api_key}' \
#                f'&redirect_uri={redirect_uri}&code={code}&grant_type=authorization_code'
#     response = req.post(api_host)
#     text = json.loads(response.text)
#     url = "https://kapi.kakao.com/v2/user/me"
#     access_token = text["access_token"]
#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }
#     user = json.loads(req.post(url=url, headers=headers).text)["kakao_account"]["profile"]
#     print(user)
#     response = render(request, 'index.html', {"name": user["nickname"], "login": True})
#     return redirect(response)


def profile(request):
    # print()
    return render(request, "index.html")
