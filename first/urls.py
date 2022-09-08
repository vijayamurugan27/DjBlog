from django.urls import path
from first import views
from first.views import PostListView

from .feeds import LatestPostsFeed

app_name = 'first'

urlpatterns = [

    path('home', views.home, name = 'home',),
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),

    # path('/post/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail1, name='post_detail'),

    path('pag_class', views.PostListView.as_view(), name='post_list'),
    path('feed/', LatestPostsFeed(), name='post_feed'),

    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
]