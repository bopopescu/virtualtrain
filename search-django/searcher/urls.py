
from django.urls import path,include
from .views import PostListView,PostDetailView,test


urlpatterns = [
    path('',PostListView.as_view(),name='home'),
    path('detail/<slug>/',PostDetailView.as_view(),name='post_detail'),
    path('test/',test,name='test')

]
