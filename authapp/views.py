from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

# Create your views here.


class check_server(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        time = datetime.now().strftime("%H:%M:%S")
        return JsonResponse({"status": "Server is running", "time":time,"stat":HTTP_200_OK}, status=HTTP_200_OK)