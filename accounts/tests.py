from django.test import TestCase, Client
from django.contrib.auth.models import User


# Create your tests here.

# setUp() 은 테스트 세팅에 사용되는 함수
# test_~() 가 실제로 구동되는 테스트 (여기서는 4개의 테스트가 구동됨)


class LoginAndLogout(TestCase):
    def setUp(self):
        self.client = Client()
        u = User.objects.create_user('test_user', 'test@example.com', 'password1') # User 객체를 임시로 생성
        u.save()

    def test_login_post(self):
        response = self.client.post("/accounts/login/", {"username": "test_user" ,"password": "password1", "next": "/"}, follow=True)
        self.assertRedirects(response, '/') # '/' 로 Post 후 Redirect 가 잘 되는지 확인(assert)
        self.assertContains(response, "test_user") # 이 때 response 에 "test_user" 가 잘 담겨있는지 확인

    def test_login_fail(self):
        response = self.client.post("/accounts/login/", {"username": "test_user1" ,"password": "password1", "next": "/"})
        self.assertContains(response, "Your username and password didn't match. Please try again.")

    def test_login_then_logout(self):
        login_response = self.client.post("/accounts/login/", {"username": "test_user" ,"password": "password1", "next": "/"}, follow=True)
        self.assertRedirects(login_response, '/')
        self.assertContains(login_response, "test_user")
        logout_response = self.client.get('/accounts/logout_view/', follow=True)
        self.assertRedirects(logout_response, '/')
        self.assertNotContains(logout_response, "test_user") # 이 때 response 에 "test_user" 가 잘 빠져있는지 확인 (assert Not contains)

class Register(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_post(self):
        response = self.client.post("/accounts/register/", {"username": "test_user" ,"password1": "password1",  "password2": "password1"}, follow=True)
        self.assertContains(response, "test_user")
        self.assertEqual(User.objects.get(username="test_user").username, "test_user") # 이 때 register 한 결과의 "test_user" 가 동일한 지 확인 (assert eqaul)
