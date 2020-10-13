from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.Client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'test@gmail.com', password = 'test@123')
        self.Client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email = 'wella@gmail.com', password = 'wella@123',
            name = 'Test user name')


    def test_users_list(self):
        url = reverse('admin:core_user_changelist')
        res = self.Client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)


    def test_user_change_page(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.Client.get(url)

        self.assertEqual(res.status_code,200)


    def test_create_user_page(self):
        url = reverse('admin: core_user_add')
        res = self.client.get('url')

        sefl.assertEqual(res.status_code, 200)
