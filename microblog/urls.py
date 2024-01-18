from django.contrib import admin
from django.urls import path

from blog.views import frontpage, post_detail

urlpatterns = [
    # ルートの設定
    path("admin/", admin.site.urls),
    path("", frontpage),
    path("<slug:slug>/", post_detail, name="post_detail")
]
