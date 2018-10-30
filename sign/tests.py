from django.test import TestCase, Client
from sign.models import Event, Guest
from django.contrib.auth.models import User
from datetime import datetime


# 创建测试
# class ModelTest(TestCase):
#     def setUp(self):
#         Event.objects.create(id=1, name='TT', limit=2000, status=True, address='abc', start_time='2018-08-28 00:00:00')
#         Guest.objects.create(id=1, event_id='1', realname='kd', phone='18989846103', email='abc@qq.com', sign=False)
#
#     def test_event_models(self):
#         result = Event.objects.get(name='TT')
#         self.assertEqual(result.address, 'abc')
#         self.assertTrue(result.status)
#
#     def test_guest_models(self):
#         result = Guest.objects.get(phone='18989846103')
#         self.assertEqual(result.realname, 'kd')
#         self.assertFalse(result.sign)

class IndexPageTest(TestCase):
    '''测试index登录首页'''

    def test_index_page_renders_index_template(self):
        '''测试index视图'''
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
    '''测试登录函数'''

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        self.c = Client()

    def test_login_action_username_password_null(self):
       '''用户名密码为空'''
       test_data = {'username':'','password':''}
       resonpse = self.c.post('/login_action', data=test_data)
       self.assertEquals(resonpse.status_code, 200)
       self.assertIn(b'username or password not null!', resonpse.content)

    def test_login_action_username_password_error(self):
       '''用户名密码错误'''
       test_data = {'username':'abc','password':'123'}
       resonpse = self.c.post('/login_action', data=test_data)
       self.assertEquals(resonpse.status_code, 200)
       self.assertIn(b'username or password Error!', resonpse.content)

    def test_login_action_success(self):
       '''登录成功'''
       test_data = {'username':'admin','password':'admin123456'}
       resonpse = self.c.post('/login_action', data=test_data)
       # 在login_action视图函数中,当用户登录验证成功后,通过HTTPresponseredurect('/event_manage/')跳转到了发布会管理视图,
       # 这是一个重定向,所以HTTP返回码是302.
       self.assertEquals(resonpse.status_code, 302)
       self.assertIn(b'Login Success!', resonpse.content)

class EventManageTest(TestCase):
    '''发布会管理'''

    def setUp(self):
        Event.objects.create(id=4,name='测试Django',limit=100,status=False,adress='USA',
                             start_time=datetime(2018,06,27,00,00,00))
        self.c = Client()

    def test_event_manage_success(self):
        '''测试发布会:测试Django'''
        response = self.c.post('/event_manage')
        self.assertEquals(response.status_code, 200)
        self.assertIn(b'测试Django', response.content)
        self.assertIn(b'USA', response.content)

    def test_event_manage_search_success(self):
        '''测试发布会搜索'''
        response = self.c.post('/search_name/', {'name':'测试Django'})
        self.assertEquals(response.status_code, 200)
        self.assertIn(b'测试Django', response.content)
        self.assertIn(b'USA', response.content)

class GuestManageTest(TestCase):
    '''嘉宾管理'''

    def setUp(self):
        Event.objects.create(id=4,name='测试Django',limit=100,status=False,adress='USA',
                             start_time=datetime(2018,06,27,00,00,00))
        Guest.objects.create(realname='gilbert',phone='15068716002',email='gilbert@qq.com',sign=0,event_id=4)
        self.c = Client()

    def test_guest_manage_success(self):
        '''测试嘉宾信息:gilbert'''
        response = self.c.post('/guest_manage')
        self.assertEquals(response.status_code, 200)
        self.assertIn(b'gilbert', response.content)
        self.assertIn(b'USA', response.content)

    def test_guest_manage_search_success(self):
        '''测试嘉宾搜索'''
        response = self.c.post('/search_phone/', {'phone':'15068716002'})
        self.assertEquals(response.status_code, 200)
        self.assertIn(b'gilbert', response.content)
        self.assertIn(b'15068716002', response.content)





















