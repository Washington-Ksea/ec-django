from django.test import TestCase
from django.core import mail
from allauth.account.forms import LoginForm, SignupForm
from allauth.utils import get_user_model
from django.contrib import auth
from django.urls import reverse
from unittest.mock import patch
from main import models

class TestSignUp(TestCase):
    def setUp(self):
        self.post_user_data = {
            "username": "username543",
            "email": "user@domain.com",
            "password1": "abcabcabc",
            "password2": "abcabcabc",
        }

    def test_user_signup_page_loads_correctly(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')
        self.assertContains(response, 'SIGN UP')
        self.assertIsInstance(
            response.context['form'], SignupForm
        )
        
    def test_user_signup_page_submission_works(self):
        post_data = self.post_user_data 
        response = self.client.post(
            reverse("account_signup"), post_data
        )
        
        #homeへリダイレクト
        self.assertEqual(response.status_code, 302)

        #ユーザが追加されたか確認
        self.assertTrue(
            models.User.objects.filter(
                email=self.post_user_data['email']
            ).exists()
        )
        #ログイン状態か
        self.assertTrue(
            auth.get_user(self.client).is_authenticated
        )

    def test_user_login_page_loads_correctly(self):
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertContains(response, 'LOGIN')
        self.assertIsInstance(
            response.context['form'], LoginForm
        )

    def test_user_login_page_submission_works(self):
        user1 = models.User.objects.create_user(
            self.post_user_data['username'],
            self.post_user_data['email'],
            self.post_user_data['password1']
        )
        user1.save()

        post_data = {
            'login':self.post_user_data['email'],
            'password':self.post_user_data['password1']    
        }

        #ユーザが追加されたか確認
        self.assertTrue(
            models.User.objects.filter(
                email=self.post_user_data['email']
            ).exists()
        )

        response = self.client.post(
            reverse("account_login"), post_data
        )

        #ログイン状態か
        self.assertTrue(
            auth.get_user(self.client).is_authenticated
        )
        
        #homeへリダイレクト
        self.assertEqual(response.status_code, 302)


        