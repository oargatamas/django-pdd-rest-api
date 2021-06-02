from django.http import HttpResponse

# Create your views here.
#from models import PricePaidData
from . import repositories, models
from . import serializers


def all_ppd(request):
    repository = repositories.FileSystemCachedCsvPpdRepository()

    result = repository.find_all_records(0,10)

    json = serializers.PricePaidDataSerializer(result, many=True)

    return HttpResponse(json.data)

def all_ppd_in_period(request, from_period, until_period):
    return HttpResponse("period: " + from_period + " to " + until_period)

def ppd_by_id(request, unique_id):
    return HttpResponse("by id: " + unique_id)