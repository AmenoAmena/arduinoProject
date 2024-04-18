from django.urls import path
from . import views 

urlpatterns = [
    path("",views.index,name = "index"),
    path("add",views.add,name = "add"),
    path("delete<int:pk>",views.delete, name = "delete"),
    path("update<int:pk>",views.update_item,name="update")
]

