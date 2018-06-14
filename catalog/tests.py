from django.test import TestCase
from django.urls import reverse
from .models import Mineral
import random

from loaddb import load_json

# Create your tests here.
class MineralDetailTestCase(TestCase):
    def setUp(self):
        load_json()
        count = len(Mineral.objects.all())
        pk = round(random.randint(0, count))
        self.mineral = Mineral.objects.get(pk=pk)            
    
    def test_detail(self):
        res = self.client.get(reverse('catalog:detail', kwargs={ 'pk': self.mineral.pk }))
        self.assertEquals(res.status_code, 200)
        self.assertContains(res, self.mineral.name)
        for key, value in self.mineral.fields_dict.items():
            self.assertContains(res, value)
    
    def test_home(self):
        res = self.client.get(reverse('catalog:home'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.mineral.name)