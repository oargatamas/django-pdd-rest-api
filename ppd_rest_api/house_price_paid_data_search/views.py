from datetime import datetime

from django.http import HttpResponse

# Create your views here.
from django.urls import reverse
from django.views import View
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import repositories
from ppd_rest_api import settings
from .models import PagingPricePaidData
from .paging import init_paging_details, set_paging_links
from rest_framework.decorators import api_view, schema

@api_view(['GET'])
def all_ppd(request):
    repository = repositories.get_repository()
    paging = init_paging_details(int(request.GET.get("pageNo", 1)))

    result = repository.find_all_records(paging.start_record,paging.end_record)

    paging.end_record = len(result)
    set_paging_links(paging, request.build_absolute_uri(reverse("get-all-ppd")))

    content = PagingPricePaidData()
    content.paging = paging
    content.price_paid_data = result
    content_serializer = serializers.PagingPricePaidDataSerializer(content, many=False)

    return Response(content_serializer.data)

@api_view(['GET'])
def all_ppd_in_period(request, from_period, until_period):
    repository = repositories.get_repository()
    paging = init_paging_details(int(request.GET.get("pageNo", 1)))

    parsed_from_period = datetime.strptime(from_period, settings.API_DATE_FORMAT)
    parsed_until_period = datetime.strptime(until_period, settings.API_DATE_FORMAT)

    result = repository.find_all_records_between(parsed_from_period, parsed_until_period, paging.start_record, paging.end_record)

    paging.end_record = len(result)
    set_paging_links(paging, request.build_absolute_uri(reverse("get-all-ppd-in-period",args=(from_period,until_period))))

    content = PagingPricePaidData()
    content.paging = paging
    content.price_paid_data = result
    content_serializer = serializers.PagingPricePaidDataSerializer(content, many=False)

    return Response(content_serializer.data)

@api_view(['GET'])
def ppd_by_id(request, unique_id):
    repository = repositories.get_repository()


    result = repository.find_record_by_id(unique_id)
    if not result:
        return Response(
            data={"message":"Record with id of " + unique_id + " not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = serializers.PricePaidDataSerializer(result[0], many=False)

    return Response(serializer.data)
