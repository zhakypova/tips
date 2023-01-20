from django.urls import path

from . import views


urlpatterns = [
    path('category/', views.CategoryListCreate.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('questions/', views.QuestionListCreate.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('questions/<int:category_id>/question/', views.QuestionAnswerList.as_view()),

]

