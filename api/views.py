from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import pytz

def home(request):
    return JsonResponse({"message": "Welcome to Retrieve Public API!"})

def public_api(request):
    response_data = {
        "email": "olakunle.adebayo77@gmail.com",
        "current_datetime": datetime.utcnow().replace(tzinfo=pytz.utc).isoformat(timespec="seconds").replace("+00:00","Z"),
        "github_url": "https://github.com/LakunleAdebayo/Retrieve-Public-API"
    }

    return JsonResponse(response_data)

