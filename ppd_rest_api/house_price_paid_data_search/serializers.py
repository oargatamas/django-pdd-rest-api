from rest_framework import serializers


class PricePaidDataSerializer(serializers.Serializer):
    transaction_unique_identifier = serializers.CharField(),
    price = serializers.DecimalField(),
    date_of_transfer = serializers.DateTimeField(),
    post_code = serializers.CharField(),
    property_type = serializers.CharField(),
    old_or_new = serializers.CharField(),
    duration = serializers.CharField(),
    paon = serializers.CharField(),
    saon = serializers.CharField(),
    street = serializers.CharField(),
    locality = serializers.CharField(),
    city = serializers.CharField(),
    district = serializers.CharField(),
    county = serializers.CharField(),
    category = serializers.CharField(),
    status = serializers.CharField()

class PagingDetailsSerializer(serializers.Serializer):
    page_number = serializers.IntegerField()
    start_record = serializers.IntegerField()
    end_record = serializers.IntegerField()
    has_next_page = serializers.BooleanField()
    has_prev_page = serializers.BooleanField()