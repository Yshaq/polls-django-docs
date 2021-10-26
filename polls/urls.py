from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    path('<int:pk>/results/', views.QuestionResultsView.as_view(), name='question-results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    

]