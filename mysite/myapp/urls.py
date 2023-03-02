from django.urls import path
from .import views

urlpatterns = [
    path("", views.display, ),
    path("page2",views.display2,)
]

