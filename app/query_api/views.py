from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from django.conf import settings
from django.http import JsonResponse
from .models import NautTemp, NautilusEncoder
from . import REDIS_INSTANCE

@api_view()
def postgres(request):
    response = NautTemp.objects.all()

    #return Response(response)
    return JsonResponse(list(response), encoder = NautilusEncoder, safe = False)

@api_view()
def redis(request):
    pipe = REDIS_INSTANCE.pipeline()

    resultSize = REDIS_INSTANCE.get("result_size")
    if resultSize is None:
        resultSize = 0
    else:
        resultSize = int(resultSize)
        
    pipe.multi()
    for i in range(0, resultSize):
        key = "result:" + str(i)
        pipe.hgetall(key)
    response = pipe.execute()
    return JsonResponse(response, encoder = NautilusEncoder, safe = False)
