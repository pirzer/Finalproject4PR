from . import views
from django.urls import path


urlpatterns = [
    path('', views.PositiveListView.as_view(), name='home'),
    path('add_positive/', views.positive, name='add_positive'),
    path('<slug:slug>/', views.PositiveDetail.as_view(), name='positive_detail'),
    path('edit-positive/<slug:slug>', views.edit_positive, name='edit_positive'),
    path('delete-positive/<slug:slug>', views.delete_positive,
         name='delete_positive'),
]
