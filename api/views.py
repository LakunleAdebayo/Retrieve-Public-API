from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import pytz

def public_api(request):
    response_data = {
        "email": "olakunle.adebayo77@gmail.com",
        "current_datetime": datetime.utcnow().replace(tzinfo=pytz.utc).isoformat(),
        "github_url": "https://github.com/LakunleAdebayo/Retrieve-Public-API"
    }
    return JsonResponse(response_data)
