from django.urls import path
from .views import index, other_page, RSLoginView, profile, RSLogoutView
from .views import ChangeUserInfoView, RSPasswordChangeView
from .views import RegisterUserView, RegisterDoneView, DeleteUserView, by_category

app_name = 'main'
urlpatterns = [
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/logout/', RSLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', RSPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', RSLoginView.as_view(), name='login'),
    path('<int:pk>/', by_category, name='by_category'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
