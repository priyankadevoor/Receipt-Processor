from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.

class ReceiptTests(APITestCase):
    def test_process_receipt(self):
        url = reverse('process_receipt')
        data = {
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
            {
            "shortDescription": "Gatorade",
            "price": "2.25"
            },{
            "shortDescription": "Gatorade",
            "price": "2.25"
            },{
            "shortDescription": "Gatorade",
            "price": "2.25"
            },{
            "shortDescription": "Gatorade",
            "price": "2.25"
            }
  ],
  "total": "9.00"
}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)

    def test_get_points(self):
        # First, create a receipt
        process_url = reverse('process_receipt')
        data = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
  ],
  "total": "35.35"
}
        process_response = self.client.post(process_url, data, format='json')
        receipt_id = process_response.data['id']

        # Now, get the points for the created receipt
        get_points_url = reverse('get_points', kwargs={'receipt_id': receipt_id})
        response = self.client.get(get_points_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('points', response.data)
