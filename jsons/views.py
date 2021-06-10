from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GiftshopSerializer
from .models import Giftshop
from rest_framework import status
# Create your views here.

# @api_view(['GET'])
# def apiView(request):
# 	api_urls = {
#     "citizens": [{
#         "citizen_id": 1,
#         "town": "Yerevan",
#         "street": "Sayat Nova",
#         "building": "16",
#         "appartement": 7,
#         "name": "Poghosyan Poghos",
#         "birth_date": "01.02.2000",
#         "gender": "male",
#         "relatives": [2, 28]
# 	},] } 
# 	return Response(api_urls)

@api_view(['GET'])
def GiftshopList(request):
	giftshop = Giftshop.objects.all().order_by('-id')
	serializer = GiftshopSerializer(giftshop, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def GiftshopDetail(request, pk):
	giftshop = Giftshop.objects.get(id=pk)
	serializer = GiftshopSerializer(giftshop, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def GiftshopCreate(request):
	serializer = GiftshopSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()


	return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
def GiftshopUpdate(request, pk, cid):
	try:
		giftshop = Giftshop.objects.get(id=pk, citizen_id=cid)
		data = request.data
		data['citizen_id'] = giftshop.citizen_id
		giftshop.town = data.get('town', giftshop.town)
		giftshop.street = data.get('street', giftshop.street)
		giftshop.building = data.get('building', giftshop.building)
		giftshop.appartement = data.get('appartement', giftshop.appartement)
		giftshop.name = data.get('name', giftshop.name)
		giftshop.birth_date = data.get('birth_date', giftshop.birth_date)
		giftshop.gender = data.get('gender', giftshop.gender)
		giftshop.relatives = data.get('relatives', giftshop.relatives)


		serializer = GiftshopSerializer(instance=giftshop,	data=data, partial=True)

		if serializer.is_valid():

		# giftshop.town = data.get('town', giftshop.town)
		# giftshop.street = data.get('street', giftshop.street)
		# giftshop.building = data.get('building', giftshop.building)
		# giftshop.appartement = data.get('appartement', giftshop.appartement)
		# giftshop.name = data.get('name', giftshop.name)
		# giftshop.birth_date = data.get('birth_date', giftshop.birth_date)
		# giftshop.gender = data.get('gender', giftshop.gender)
		# giftshop.relatives = data.get('relatives', giftshop.relatives)

			serializer.save()
		return Response(serializer.data)
	except:
		return Response("You Can't Change *id* and *citizen_id* fields or Something went wrong,try again")
	

@api_view(['DELETE'])
def GiftshopDelete(request, pk):
	giftshop = Giftshop.objects.get(id=pk)
	giftshop.delete()
	return Response('Item Deleted Succesfully')
