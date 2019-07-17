from django.test import TestCase
from .serializers import *
from .views import *
import collections
from .admin import *
from django.contrib.admin.sites import AdminSite
from django.test.client import RequestFactory

# Create your tests here.
class TestSerializers(TestCase):

    def setUp(self):
        o = Menu.objects.create(
            id = 10,
            name = 'menu_name',
            description = 'menu_description',
        )
        Dish.objects.create(
            id = 10,
            name = 'dish_name',
            description = 'dish_description',
            menu_id = o
        )

    def test_convert_datetime(self):
        _datetime = datetime.datetime(2019, 7, 10, 12, 13, 14, 0, tzinfo=pytz.utc)
        new_datetime = convert_datetime(_datetime)
        self.assertEqual(new_datetime, '2019/07/10 14:13:14')

    def test_menu_serializer(self):
        menus = Menu.objects.all().values()
        created = convert_datetime(menus[0]['created'])
        modified = convert_datetime(menus[0]['modified'])
        menus_serialized = MenuSerializer(menus, many=True).data
        test_data = collections.OrderedDict()
        test_data['id'] = 10
        test_data['name'] = 'menu_name'
        test_data['description'] = 'menu_description'
        test_data['created'] = created
        test_data['modified'] = modified
        self.assertEqual(menus_serialized, [test_data])

    def test_dish_serializer(self):
        dishes = Dish.objects.all().values()
        created = convert_datetime(dishes[0]['created'])
        modified = convert_datetime(dishes[0]['modified'])
        dishes_serialized = DishSerializer(dishes, many=True).data
        test_data = collections.OrderedDict()
        test_data['id'] = 10
        test_data['name'] = 'dish_name'
        test_data['description'] = 'dish_description'
        test_data['preparation_time'] = None
        test_data['is_vegetarian'] = False
        test_data['created'] = created
        test_data['modified'] = modified
        test_data['image'] = ''
        self.assertEqual(dishes_serialized, [test_data])


class TestView(TestCase):

    def setUp(self):
        o = Menu.objects.create(
            id = 10,
            name = 'menu_name',
            description = 'menu_description',
        )
        Dish.objects.create(
            id = 10,
            name = 'dish_name',
            description = 'dish_description',
            menu_id = o
        )
        self.factory = RequestFactory()

    def get_test_menu_dict(self):
        menus = Menu.objects.all().values()
        created = convert_datetime(menus[0]['created'])
        modified = convert_datetime(menus[0]['modified'])
        test_data = collections.OrderedDict()
        test_data['id'] = 10
        test_data['name'] = 'menu_name'
        test_data['description'] = 'menu_description'
        test_data['created'] = created
        test_data['modified'] = modified
        test_data['num_dishes'] = 1
        return test_data

    def test_get_menu(self):
        request = self.factory.get('/get_menu')
        response = get_menu(request)
        test_data = self.get_test_menu_dict()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [test_data])

    def test_get_menu_detail(self):
        data = {'id': 10}
        request = self.factory.post('/get_menu_detail', data)
        response = get_menu_detail(request)
        dishes = Dish.objects.all().values()
        created = convert_datetime(dishes[0]['created'])
        modified = convert_datetime(dishes[0]['modified'])
        dishes_serialized = DishSerializer(dishes, many=True).data
        test_data = collections.OrderedDict()
        test_data['id'] = 10
        test_data['name'] = 'dish_name'
        test_data['description'] = 'dish_description'
        test_data['preparation_time'] = None
        test_data['is_vegetarian'] = False
        test_data['created'] = created
        test_data['modified'] = modified
        test_data['image'] = ''
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [test_data])

    def test_main_page(self):
        request = self.factory.get('')
        response = main_page(request)
        self.assertEqual(response.status_code, 200)
