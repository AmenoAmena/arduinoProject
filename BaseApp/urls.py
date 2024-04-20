from django.urls import path
from . import views 

urlpatterns = [
    path("",views.index,name = "index"),
    path("add",views.add,name = "add"),
    path("delete<int:pk>",views.delete, name = "delete"),
    path("update<int:pk>",views.update_item,name="update"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

