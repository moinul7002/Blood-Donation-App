import imp
import json
from urllib import response

from django.urls import reverse
from requests import request
import requests
from rest_framework import status
from rest_framework.test import APITestCase
from .api.serializers import *
from .models import *

class DonorListTestCase(APITestCase):

    def setUp(self):
        self.user = Donor.objects.create(firstname='Moinul',lastname='Islam',age='24',sex='Male',blood_group='OPOS')

    def test_donor_list(self):
        response = self.client.get("/api/list-of-donors/")
        self.assertEqual(response.status_code, 200)
    
    def test_donor_list_reverse(self):
        response = self.client.get(reverse("list-of-donor"))
        self.assertEqual(response.status_code, 200)

class DonorFormViewTestCase(APITestCase):

    def test_donor_submit(self):
        data={'firstname':'sam','lastname':'kabir','age':'24','sex':'Male','location':'Dhaka','blood_group':'OPOS'}
        response = self.client.post("/api/donor/",data)
        self.assertEqual(response.status_code, 201)
    
    def test_donor_invalid_submit(self):
        data={'firstname':'sam','lastname':'kabir','age':'Twenty Four','sex':'Male','location':'Dhaka','blood_group':'OPOS'}
        response = self.client.post("/api/donor/",data)
        self.assertEqual(response.status_code, 400)

    def test_donor_empty_submit(self):
        data={'firstname':' ','lastname':' ','age':' ','sex':' ','location':' ','blood_group':' '}
        response = self.client.post("/api/donor/",data)
        self.assertEqual(response.status_code, 400)
    
    def test_donor_incomplete_submit(self):
        data={'firstname':'sam','lastname':'kabir'}
        response = self.client.post("/api/donor/",data)
        self.assertEqual(response.status_code, 400)

    def test_donor_partial_submit(self):
        data={'firstname':'sam','lastname':'kabir','age':'','sex':'','location':'','blood_group':''}
        response = self.client.post("/api/donor/",data)
        self.assertEqual(response.status_code, 201)


class SearchViewTestCase(APITestCase):

    def setUp(self):
        self.user = Donor.objects.create(firstname='Moinul',lastname='Islam',age='24',sex='Male',blood_group='OPOS')

    def test_search_No_content(self):
        data={'q':'Khulna'}
        response = self.client.get("/api/search/",data)
        self.assertEqual(response.status_code, 204)

    def test_search_No_content_incomplete_keywords(self):
        data={'q':'A'}
        response = self.client.get("/api/search/",data)
        self.assertEqual(response.status_code, 204)

    def test_search_success(self):
        data={'q':'24'}
        response = self.client.get("/api/search/",data)
        self.assertEqual(response.status_code, 200 )

    def test_search_success_multi_field(self):
        data={'q':'24 Male'}
        response = self.client.get("/api/search/",data)
        self.assertEqual(response.status_code, 200 )

    def test_search_fail_multi_field(self):
        data={'q':'24 Male Chittagong'}
        response = self.client.get("/api/search/",data)
        self.assertEqual(response.status_code, 204 )
