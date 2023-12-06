from django.urls import path
from .views import PostWord

urlpatterns = [
    path("post_word/", PostWord.as_view(), name="post"),
]
