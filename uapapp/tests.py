# from django.contrib.auth.models import User
# from django.conf import settings
# from django.test import TestCase, Client
# from django_seed import Seed
# from uapapp.models import Dependencia, Programa
# from jwt import decode


# class Dependencies(TestCase):
#     def setUp(self):        
#         seeder = Seed.seeder()
#         seeder.add_entity(Dependencia, 5)
#         seeder.execute()
    
#     def test_dependencies_got_name(self):
#         for depen in Dependencia.objects.all():
#             self.assertGreaterEqual(len(depen.nombre), 1)


# class Programs(TestCase):
#     def setUp(self):
#         seeder = Seed.seeder()
#         seeder.add_entity(Dependencia, 5)
#         seeder.execute()

#         seeder = Seed.seeder()
#         seeder.add_entity(Programa, 5)
#         seeder.execute()
    
#     def test_programs_got_name(self):
#         for prog in Programa.objects.all():
#             self.assertGreaterEqual(len(prog.nombre), 1)

#     def test_programs_got_depen(self):
#         for prog in Programa.objects.all():
#             self.assertGreaterEqual(prog.dependencia.pk, 0)

#     def test_programs_got_type(self):
#         for prog in Programa.objects.all():
#             self.assertLessEqual(len(prog.tipo), 3)

# class Permissions(TestCase):
#     def setUp(self):
#         seeder = Seed.seeder()
#         seeder.add_entity(Dependencia, 5)
#         seeder.execute()

#         seeder = Seed.seeder()
#         seeder.add_entity(Programa, 5)
#         seeder.execute()

#         self.user_no_permissions = User.objects.create_user(
#             username='test', email='test@test.com', password='my_secret_test')
        
#     def test_api_key_no_p(self):
#         c = Client()
#         resquest = c.post('/api/token/', {'username':'test', 'password':'my_secret_test'})
#         rjwt_dec_access = decode(resquest.json()['access'], settings.SECRET_KEY)
#         rjwt_dec_refresh = decode(resquest.json()['refresh'], settings.SECRET_KEY)
#         self.assertEqual(len(rjwt_dec_access['groups']), 0)
#         self.assertEqual(len(rjwt_dec_refresh['groups']), 0)
    
#     def test_api_unauthorized(self):
#         client = Client()
#         resquest = client.post('/api/token/', {'username':'test', 'password':'nel'})
#         self.assertEqual(resquest.status_code, 401)
