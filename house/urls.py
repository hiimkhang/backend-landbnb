from django.urls import path
from . import views 

app_name = "houses"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>", views.HouseDetail.as_view(), name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
]