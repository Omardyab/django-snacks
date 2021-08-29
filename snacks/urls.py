from django.urls import path
#  add new urls here for home page and about page
from .views import HomePageView, AboutPageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]