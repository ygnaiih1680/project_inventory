from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', include("main.urls")),
    path('book/', include("book.urls")),
    path("library/", include("library.urls")),
]
