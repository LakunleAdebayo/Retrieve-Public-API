from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import pytz

def public_api(request):
    response_data = {
        "email": "olakunle.adebayo@gmail.com",
        "current_datetime": datetime.utcnow().replace(tzinfo=pytz.utc).isoformat(),
        "github_url": "https://github.com/LakunleAdebayo/your-repo"
    }
    return JsonResponse(response_data)
