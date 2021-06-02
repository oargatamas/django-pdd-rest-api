from datetime import datetime

from django.http import HttpResponse

# Create your views here.
from rest_framework import renderers, response

from . import repositories, models
from . import serializers
from . import repositories
from ppd_rest_api import settings


def all_ppd(request):
    repository = repositories.get_repository()

    result = repository.find_all_records(0, 10)
    serializer = serializers.PricePaidDataSerializer(result, many=True)
    render = renderers.JSONRenderer()

    return HttpResponse(
        status=200,
        content_type="application/json",
        content=render.render(serializer.data),
    )


def all_ppd_in_period(request, from_period, until_period):
    repository = repositories.get_repository()

    parsed_from_period = datetime.strptime(from_period, settings.API_DATE_FORMAT)
    parsed_until_period = datetime.strptime(until_period, settings.API_DATE_FORMAT)

    result = repository.find_all_records_between(parsed_from_period, parsed_until_period, 0, 10)
    serializer = serializers.PricePaidDataSerializer(result, many=True)
    render = renderers.JSONRenderer()

    return HttpResponse(
        status=200,
        content_type="application/json",
        content=render.render(serializer.data)
    )


def ppd_by_id(request, unique_id):
    repository = repositories.get_repository()

    result = repository.find_record_by_id(unique_id)
    if not result:
        return HttpResponse(
            status=404,
            content_type="application/json",
        )

    serializer = serializers.PricePaidDataSerializer(result[0], many=False)
    render = renderers.JSONRenderer()

    return HttpResponse(
        status=200,
        content_type="application/json",
        content=render.render(serializer.data),
    )
