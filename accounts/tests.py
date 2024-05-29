from django.test import TestCase, Client
from django.urls import reverse
from book_store.settings import BASE_URL

import pytest
import unittest

client = Client()


@pytest.mark.django_db
class test_TestURLs(unittest.TestCase):

    def test_RegistarationOnSubmit_ThenReturn_HTTP_406_NOT_ACCEPTABLE(self):
        url = BASE_URL + reverse("register")
        userData = {'first_name': '', 'last_name': '', 'phone_number': '',
                    'password1': '', 'password2': '', 'email': ''}

        response = client.post(path=url, data=userData, format='json')

        self.assertEqual(response.status_code, 406)

    def test_RegistarationOnSubmit_ThenReturn_HTTP_200_OK(self):
        url = BASE_URL + reverse("register")
        userData = {'first_name': 'Rakhi', 'last_name': 'R', 'phone_number': '9887889767',
                    'password1': 'Rakhikumar@123', 'password2': 'Rakhikumar@123', 'email': 'rakesh333@gmail.com'}

        response = client.post(path=url, data=userData, format='json')

        self.assertEqual(response.status_code, 200)

    def test_LoginOnSubmit_ThenReturn_HTTP_200_OK(self):
        url = BASE_URL + reverse("login")
        userData = {'phone_number': '9887889767', 'password': 'Rakhikumar@123'}

        response = client.post(path=url, data=userData, format='json')

        self.assertEqual(response.status_code, 200)