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
    path('part4/', views.part4_IndexView.as_view(), name='part4_index'),
    path('part4/<int:pk>/', views.part4_DetailView.as_view(), name='part4_detail'),
    path('part4/<int:pk>/results/', views.part4_ResultsView.as_view(), name='part4_results'),
    path('part4/<int:question_id>/vote/', views.part4_vote, name='part4_vote'),
    path('',views.tutorials,name="tutorials")
]