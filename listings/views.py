from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReservationSerializer,BookingInfoSerializer
from .models import Reservation,BookingInfo


@api_view(['GET','POST'])
def reservation(request):

    if request.method == 'GET':
        queryset = Reservation.objects.all()
        filterset = ReservationFilter(request.GET, queryset=queryset)
        if filterset.is_valid():
            queryset = filterset.qs
        serializer = ReservationSerializer(queryset,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def get_booking_info(request):

    check_in = request.query_params.get('check_in', None)
    check_out = request.query_params.get('check_out', None)
    max_price = request.query_params.get('max_price', None)

    queryset = BookingInfo.objects.exclude(
        reservation_info__check_in__gte=check_in,
        reservation_info__check_out__lte=check_out,
    ).filter(price__lt=max_price)

    serializer = BookingInfoSerializer(queryset,many=True)
    return Response(serializer.data)
    