from django.http import JsonResponse

def api_home(request,  *args, **kwargs):
    
   return JsonResponse({"error":"no request sent"})