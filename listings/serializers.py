from rest_framework import serializers
from .models import Listing, HotelRoomType, HotelRoom, BookingInfo, Reservation


class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = '__all__'


class HotelRoomTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelRoomType
        fields = '__all__'


class HotelRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelRoom
        fields = '__all__'


class BookingInfoSerializer(serializers.ModelSerializer):
    listing = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = BookingInfo
        fields = '__all__'

    def get_listing(self,obj):
        return ListingSerializer(obj.listing).data


class ReservationSerializer(serializers.ModelSerializer):
    booking_info = BookingInfoSerializer()

    class Meta:
        model = Reservation
        fields = ('booking_info','check_in','check_out')