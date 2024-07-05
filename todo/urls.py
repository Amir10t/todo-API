from django.urls import path
from todo import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('todos/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('todos/schema/', SpectacularAPIView.as_view(), name='schema'),
    path("todos/drf/", views.TodoListAPIView.as_view()),
    path("todos/drf/<pk>", views.TodoDetailAPIView.as_view()),
]
