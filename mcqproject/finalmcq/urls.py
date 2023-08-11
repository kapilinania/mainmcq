from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index_view, name='index'),
    path('', views.get_network_info, name='network_info'),
    path('exam-start/', views.start_exam, name='start_exam'),
    path('delete-data/', views.delete_data, name='delete_data'),

]