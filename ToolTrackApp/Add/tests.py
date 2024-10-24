# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from ToolTrackApp.Room.models import Room
import json
from ToolTrackApp.Borrow.models import Item

class AddItemTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('add_item')
        self.room = Room.objects.create(number=302)
    
    def test_add_item_success(self):
        data = {
            'name': 'Test Tool',
            'roomId': self.room.number,
            'amount': 2
        }
        response = self.client.post(self.url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Item.objects.filter(name='Test Tool').count(), 2)
        self.assertEqual(self.room.items.filter(name='Test Tool').count(), 2)

    def test_add_item_missing_name(self):
        data = {
            'roomId': self.room.number,
            'amount': 2
        }
        response = self.client.post(self.url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], 'Name is required')
