from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from main import models


@api_view(['GET'])
def list_masques(request):
    masjid_list = []
    masques = models.Masque.objects.all()
    for masque in masques:
        image_masque = models.ImageMasque.objects.filter(masqueimg=masque)
        masque.image = image_masque
        masjid_list.append(masque)
    serializer_masque = serializers.MasqueSer(masjid_list, many=True)    
    context = {
            'masque':serializer_masque.data,
            }
    return Response(context)


@api_view(['GET'])
def masque_detail(request, pk):
    masque = models.Masque.objects.get(pk=pk)
    prayert = models.PrayerTime.objects.get(masquet=masque)
    staffs = models.Staff.objects.filter(masque=masque)
    image_masque = models.ImageMasque.objects.filter(masqueimg=masque)
    
    serializer_image = serializers.ImageMasqueSer(image_masque, many=True)
    serializer_prayert = serializers.PrayerTimeeSer(prayert)
    serializer = serializers.MasqueSer(masque)
    serializer_staff = serializers.StaffSer(staffs, many=True)
    context = {
        'masque':serializer.data,
        'image':serializer_image.data,
        'staff':serializer_staff.data,
        'prayert':serializer_prayert.data
    }
    return Response(context)


