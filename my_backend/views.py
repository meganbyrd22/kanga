from django.http import JsonResponse

def endpoint1(request):
    data = {
        "message": "Hello from Endpoint 1"
    }
    return JsonResponse(data)

def endpoint2(request):
    data = {
        "message": "Hello from Endpoint 2"
    }
    return JsonResponse(data)
