from . import views
from django.urls import path

# added EventList, Suggestion, EventOverview, EventJoin, UpdateEvent, DeleteEvent
# path('suggestE/', views.Suggestion.as_view(), name='suggestion'),

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path("", views.EventList.as_view(), name="home"),
    path('suggestion', views.Suggestion.as_view(), name='suggestion'),
    path('<slug:slug>/', views.EventOverview.as_view(), name='event_detail'),
    path('join/<slug:slug>', views.EventJoin.as_view(), name='event_join'),
    path('update/<slug:slug>', views.UpdateEvent.as_view(), name='update'),
    path('delete/<slug:slug>', views.DeleteEvent.as_view(), name='delete'),
]
