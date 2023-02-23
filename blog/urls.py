from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='about-page'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='detail-post'),
    path('post/create-post', views.PostCreateView.as_view(), name='create-post'),
    # path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='update-post'),
    # path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete-post')
]