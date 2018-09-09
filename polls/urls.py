from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('part1/', views.index, name='index'),
    path('part2/', views.part2, name='part2'),
    path('part3/', views.part3_index, name='part3_index'),
    path('part3/<int:question_id>/', views.part3_detail, name='part3_detail'),
    path('part3/<int:question_id>/results/', views.part3_results, name='part3_results'),
    path('part3/<int:question_id>/vote/', views.part3_vote, name='part3_vote'),
]