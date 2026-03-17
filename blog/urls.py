from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    # path("post/list", views.post_list, name="post_list"),
    path("post/list", views.PostListView.as_view(), name="post_list"),
    # path("post/create", views.post_create, name="post_create"),
    path("post/create", views.PostCreateView.as_view(), name="post_create"),
    path("post/update/<int:pk>", views.PostUpdateView.as_view(), name="post_update"),
    path("post/detail/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
    path("post/delete/<int:pk>", views.PostDeleteView.as_view(), name="post_delete"),
]
