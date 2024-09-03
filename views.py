from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import UserReadStatus
from .config import USER_MODEL

class ReadStatusView(View):

    def get(self, request, user_id):
        user = get_object_or_404(USER_MODEL, id=user_id)
        read_status, created = UserReadStatus.objects.get_or_create(user=user)
        return JsonResponse({'is_read': read_status.is_read})

    def post(self, request, user_id):
        user = get_object_or_404(USER_MODEL, id=user_id)
        read_status, created = UserReadStatus.objects.get_or_create(user=user)
        read_status.is_read = True
        read_status.save()
        return JsonResponse({'is_read': read_status.is_read})
