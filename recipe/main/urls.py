from django.urls import path
from .views import index, other_page, RSLoginView, profile, RSLogoutView, ChangeUserInfoView, RSPasswordChangeView

app_name = 'main'
urlpatterns = [
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/logout/', RSLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', RSPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', RSLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
