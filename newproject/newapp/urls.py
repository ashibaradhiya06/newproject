from django.urls import path
from newapp import views
urlpatterns=[
    path("",views.Navbar,name="navbar"),
    path("data/",views.Data,name="data"),
    path("form/",views.Form,name="form"),
    path("delete/<int:id>/",views.Delete,name="delete"),
    path("update/<int:id>/",views.Update,name="update")
]