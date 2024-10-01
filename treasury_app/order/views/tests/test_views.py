from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ...models import Order

# NOTE: Only created order test cases as an example 

class OrderViewTests(APITestCase):
    def setUp(self):
        self.order = Order.objects.create(
            term='10Y',
            amount=10000.00,
            yield_rate=4.5,
            order_status='submitted'
        )

        self.create_url = reverse('create_order')
        self.list_url = reverse('list_orders')
        self.show_url = reverse('show_order', kwargs={'id': self.order.id})
        self.update_url = reverse('update_order', kwargs={'id': self.order.id})
        
        self.order_payload = {
            'term': '5Y',
            'amount': 15000.00,
            'yield_rate': 3.7,
            'order_status': 'submitted',
        }

    def test_create_order(self):
        response = self.client.post(self.create_url, self.order_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)
        self.assertEqual(Order.objects.get(pk=response.data['id']).term, '5Y')

    def test_list_orders(self):
        response = self.client.get(self.list_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['term'], '10Y')

    def test_update_order(self):
        update_payload = {
            'term': '2Y',
            'amount': 20000.00,
            'yield_rate': 2.8,
            'order_status': 'approved',
        }
        response = self.client.put(self.update_url, update_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_order = Order.objects.get(id=self.order.id)

        self.assertEqual(updated_order.term, '2Y')
        self.assertEqual(updated_order.amount, 20000.00)
        self.assertEqual(updated_order.order_status, 'approved')
