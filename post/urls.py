from django.urls import path 
from . views import all_post, post_detail,filter_post, search_result,contactView, successView, index

urlpatterns = [
	path('', index, name="index"),
	path('research_papers/', all_post, name="all_post"),
	path('post/<int:id>/', post_detail, name="post_detail"),
	path('post/<str:subject>/', filter_post, name="filter_post"),
	path('search/', search_result, name='search_results'),
	path('contact/', contactView, name='contact'),
	path('success/', successView, name='success'),
]