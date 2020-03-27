from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.firstview),
    # ex: /polls/5/
    path('FlashCard/<title>/', views.bulletpoints),
    path('flashcards/', views.flashcards),
    path('createflashcard/', views.createflashcard),
    path('createflashcardform/',views.createflashcardform),
    path('editFlashcard/<title>/', views.editFlashcard),

# addbulletpointonFlashcard
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]