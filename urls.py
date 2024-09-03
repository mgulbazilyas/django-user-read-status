from django.urls import path
from .views import ReadStatusView, ResetReadStatusView, ResetUserReadStatusView

urlpatterns = [
    path('read-status/<int:user_id>/', ReadStatusView.as_view(), name='read_status'),
    path('reset-read-status/', ResetReadStatusView.as_view(), name='reset_read_status'),
    path('reset-read-status/<int:user_id>/', ResetUserReadStatusView.as_view(), name='reset_user_read_status'),
]
