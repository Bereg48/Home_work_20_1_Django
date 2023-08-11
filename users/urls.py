from django.urls import path

from users.apps import UsersConfig
from users.views import LogoutView, LoginView

app_name = UsersConfig

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

