from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import uuid
import math

# Create your views here.

receipts_store = {}

def getPoints(receipt_data):
    
    points = 0
    retailer = receipt_data['retailer'].strip()
    total = float(receipt_data['total'])
    num_of_items = len(receipt_data['items'])
    date = int(receipt_data['purchaseDate'][-2:])
    time = int(receipt_data['purchaseTime'][:2])

    #Rule 1
    for c in retailer:
        if c.isalnum():
            points += 1
    #Rule 2
    if total == int(total):
        points += 50
    #Rule 3
    if total % 0.25 ==0:
        points += 25
    #Rule 4
    points += (num_of_items // 2) * 5
    #Rule 5
    for item in receipt_data['items']:
        desc = item['shortDescription'].strip()
        price = float(item['price'])
        if len(desc) % 3 == 0:
            points += math.ceil(price * 0.2)
    #Rule 6
    if date % 2 != 0:
        points += 6
    #Rule 7
    if time >= 14 and time < 16:
        points += 10

    return points

@api_view(['POST'])
def process_receipt(request):
    try:
        receipt_data = request.data
        receipt_id = str(uuid.uuid4())
        points = getPoints(receipt_data)
        receipts_store[receipt_id] = points
        return Response({'id': receipt_id}, status=status.HTTP_201_CREATED)
    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_points(request, receipt_id):
    points = receipts_store.get(receipt_id)
    if points:
        return Response({'points':points})
    else:
        return Response({'error':'Receipt Not Found'}, status = status.HTTP_404_NOT_FOUND)
