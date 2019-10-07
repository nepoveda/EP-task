from django.urls import path

from .views import ArticleDetailView

app_name = 'linux_in_schools'
urlpatterns = [
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
