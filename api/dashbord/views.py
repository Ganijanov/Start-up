from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from main import models

@api_view(['POST'])
def create_country(request):
    try:
        name = request.data['name']
        models.Cauntry.objects.create(
            name=name
        )
        data = {'success':True}
    except:
        data = {'success':False}
    return Response(data)


@api_view(["POST"])
def update_country(request, pk):
    country = models.Cauntry.objects.get(pk=pk)
    
    country.name = request.data['name']
    country.save()
    data = {'success':True}
    return Response(data)


@api_view(['GET'])
def delate_country(request, pk):
    country = models.Cauntry.objects.get(pk=pk)
    try:
        country.delete()
        data = {'success':True}
    except:
        data = {'success':False}
    return Response(data)


@api_view(['POST'])
def create_city(request):
    try:
        name = request.data['name']
        country = models.Cauntry.objects.get(name=request.data['cauntry'])
        models.City.objects.create(
            name=name,
            cauntry=country
        )
        data = {'success':True}
    except:
        data = {'success':False}
    return Response(data)


@api_view(["POST"])
def update_city(request, pk):
    city = models.City.objects.get(pk=pk)
    try:
        city.name = request.data['name']
        city.cauntry = models.Cauntry.objects.get(name=request.data['cauntry'])
        city.save()
        data = {'success': True}
    except:
        data = {'success':False, 'status': 'sizda bu huquq yoq'}
    return Response(data)


@api_view(['GET'])
def delate_city(request, pk):
    city = models.City.objects.get(pk=pk)
    try:
        city.delete()
        data = {'success':True}
    except:
        data = {'success':False}
    return Response(data)


@api_view(['POST'])
def create_staff(request):
    try:      
        f_name = request.data['f_name']
        l_name = request.data['l_name']
        staff = request.data['staff']
        bio = request.data['bio']
        image = request.data['image']
        masque = models.Masque.objects.get(name=request.data['masque'])
        models.Staff.objects.create(
        f_name = f_name,
        l_name = l_name,
        staff = staff,
        bio = bio,
        image = image,
        masque = masque
        )
        data = {'status': True}
    except:
        data = {'status': False}
    return Response(data)


@api_view(['POST'])
def update_staff(request, pk):
    staff = models.Staff.objects.get(pk=pk)
    if staff.masque.admin == request.user:
        try:
            staff.f_name = request.data['f_name']
            staff.l_name = request.data['l_name']
            staff.staff = request.data['staff']
            staff.bio = request.data['bio']
            staff.image = request.data['image']
            staff.masque = models.Masque.objects.get(name=request.data['masque'])
            staff.save()
            data = {'status': True}
        except:
            data = {'status': False}
    else:
        data = {'status' : 'Sizda bu huquq yoq'}
    return Response(data)


@api_view(['GET'])
def delate_staff(request, pk):
    staff = models.Staff.objects.get(pk=pk)
    if staff.masque.admin == request.user:
        try:
            staff.delete()
            data = {'status': True}
        except:
            data = {'status': False}
    else:
        data = {'status' : 'Sizda bu huquq yoq'}
    return Response(data)


@api_view(['POST'])
def create_masque(request):
    try:
        admin = models.User.objects.get(username=request.user.username)
        name = request.data['name']
        city = models.City.objects.get(name=request.data['city'])
        capacity = request.data['capacity']
        bio = request.data['bio']
        models.Masque.objects.create(
            admin=admin, 
            name=name,
            city=city,
            capacity=capacity,
            bio=bio
        )
        data = {"Success": True}
    except:
        data = {"Success": False}
    return Response(data)


@api_view(['POST'])
def update_masque(request, pk):
    masque = models.Masque.objects.get(pk=pk)

    if masque.admin == request.user:
        masque.name = request.data['name']
        masque.city = models.City.objects.get(name=request.data['city'])
        masque.capacity = request.data['capacity']
        masque.bio = request.data['bio']
        masque.save()
        data = {"Success":True}
    else:
        data = {"Success": False}
    return Response(data)


@api_view(['GET'])
def delate_masque(request, pk):
    masque = models.Masque.objects.get(pk=pk)

    if masque.admin.username == request.user.username:
        try:
            masque.delete()
            data = {"Success":True}
        except:
            data = {'Success': False}    
    else:
        data = {"Success": 'Sizda bu huquq yoq'}
    return Response(data)