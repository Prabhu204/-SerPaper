from django.urls import path 
from . views import all_post, post_detail,filter_post, TaskSearch,contactView, successView

urlpatterns = [
	path('', all_post, name="all_post"),
	path('post/<int:id>/', post_detail, name="post_detail"),
	path('post/<str:subject>/', filter_post, name="filter_post"),
	path('search/', TaskSearch.as_view() , name='search_results'),
	path('contact/', contactView, name='contact'),
	path('success/', successView, name='success'),
]