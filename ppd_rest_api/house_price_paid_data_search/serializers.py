from django.conf import settings
from rest_framework import serializers


class PricePaidDataSerializer(serializers.Serializer):
    id = serializers.CharField()
    price = serializers.DecimalField(max_digits=100,decimal_places=2)
    date_of_transfer = serializers.DateTimeField(format=settings.DATE_FORMAT)
    post_code = serializers.CharField(max_length=100)
    property_type = serializers.CharField(max_length=100)
    old_or_new = serializers.CharField(max_length=100)
    duration = serializers.CharField(max_length=100)
    paon = serializers.CharField(max_length=100)
    saon = serializers.CharField(max_length=100)
    street = serializers.CharField(max_length=100)
    locality = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    district = serializers.CharField(max_length=100)
    county = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=100)

class PagingDetailsSerializer(serializers.Serializer):
    page_number = serializers.IntegerField()
    start_record = serializers.IntegerField()
    end_record = serializers.IntegerField()
    next_page = serializers.CharField(max_length=500)
    prev_page = serializers.CharField(max_length=500)

class PagingPricePaidDataSerializer(serializers.Serializer):
    paging = PagingDetailsSerializer()
    price_paid_data = PricePaidDataSerializer(many=True)