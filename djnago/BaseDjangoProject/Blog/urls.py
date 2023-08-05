from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="Blog-Homepage"),
    path("user/<username>/", UserPostListView.as_view(), name="User-Post"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="Post_Detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="Post-Update"),
    path("post/<int:pk>/del/", PostDeleteView.as_view(), name="Post-Delete"),
    path("post/new/", PostCreateView.as_view(), name="Create_Post"),
    path("about/", views.about, name="Blog-About")
]