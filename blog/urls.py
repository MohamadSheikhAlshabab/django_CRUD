from django.urls import path
from .views import HomeView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns =[
        path('home',HomeView.as_view(),name='home'),
        path('post/<int:pk>',BlogDetailView.as_view(),name='Blog_details'),
        path('post/new',BlogCreateView.as_view(),name='create_view'),
        path('post/<int:pk>/update',BlogUpdateView.as_view(),name='update_view'),
        path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='delete_view')
]