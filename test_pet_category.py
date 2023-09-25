from api import PetCategory
from settings import valid_username, valid_password
import os

pc = PetCategory()

def test_add_pet_to_category(self):
        category = PetCategory("Cats")
        pet = "Fluffy"
        category.add_pet(pet)
        self.assertEqual(len(category.pets), 1)
        self.assertIn(pet, category.pets)

def test_remove_pet_from_category(self):
        category = PetCategory("Birds")
        pet = "Polly"
        category.add_pet(pet)
        category.remove_pet(pet)
        self.assertEqual(len(category.pets), 0)
        self.assertNotIn(pet, category.pets)

def test_get_api_key_for_valid_user(email=valid_username, password=valid_password):
    status, result = pc.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pc.get_api_key(valid_username, valid_password)
    status, result = pc.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Барсик', pet_photo='images/19.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pc.get_api_key(valid_username, valid_password)

    status, result = pc.add_new_pet(auth_key, name, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    _, auth_key = pc.get_api_key(valid_username, valid_password)
    _, my_pets = pc.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pc.add_new_pet(auth_key, "Суперкот", "images/19.jpg")
        _, my_pets = pc.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pc.delete_pet(auth_key, pet_id)

    _, my_pets = pc.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик'):
    _, auth_key = pc.get_api_key(valid_username, valid_password)
    _, my_pets = pc.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pc.update_pet_info(auth_key, my_pets['pets'][0]['id'], name)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("Это не мой питомец")


def test_add_pet_with_a_lot_of_words_in_variable_animal_type(name='Барсик',  age='4', pet_photo='images/19.jpg'):
    animal_type = 'игиенический наполнитель Барсик «Рыжий» – экологически чистый высококачественный впитывающий наполнитель для кошачьего туалета, ' \
                  'изготовлен из природного минерала – опоковидной глины, прошедшей специальную технологическую обработку.'

    _, auth_key = pc.get_api_key(valid_username, valid_password)
    status, result = pc.add_new_pet(auth_key, name, pet_photo)

    list_animal_type = result['animal_type'].split()
    word_count = len(list_animal_type)

    assert status == 200
    assert word_count < 10, 'Питомец добавлен с названием породы больше 10 слов'


def test_add_pet_with_special_characters_in_variable_animal_type(name='Барсик', pet_photo='images/19.jpg'):
    animal_type = 'Cat%@'
    symbols = '#$%^&*{}|?/><=+_~@'
    symbol = []

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pc.get_api_key(valid_username, valid_password)
    status, result = pc.add_new_pet(auth_key, name,  pet_photo)

    assert status == 200
    for i in symbols:
        if i in result['animal_type']:
            symbol.append(i)
    assert symbol[0] not in result['animal_type'], 'Питомец добавлен с недопустимыми символами'


def test_add_pet_with_empty_value_in_variable_name(name=' ', pet_photo='images/19.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pc.get_api_key(valid_username, valid_password)
    status, result = pc.add_new_pet(auth_key, name, pet_photo)
    assert status == 200
    assert result['name'] != '', 'Питомец добавлен на сайт с пустым значением в имени'


def test_add_pet_negative_age_number(name='Барсик',  age='-4', animal_type='кот', pet_photo='images/19.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pc.get_api_key(valid_username, valid_password)
    _, result = pc.add_new_pet(auth_key, name, animal_type, pet_photo)

    assert age not in result['age'], 'Питомец добавлен на сайт с отрицательным числом в поле возраст'


def test_add_photo_at_pet(name='Барсик', pet_photo='images/20.jpeg'):
    _, auth_key = pc.get_api_key(valid_username, valid_password)
    _, my_pets = pc.get_list_of_pets(auth_key, 'my_pets')
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    pet_id = my_pets['pets'][0]['id']
    status, result = pc.add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 200
    assert result['pet_photo'] != pet_photo

def test_add_new_pet_with_no_data(name='', animal_type='', age=''):

    _, auth_key = pc.get_api_key(valid_username, valid_password)

    status, result = pc.add_new_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == ''
    assert result['pet_photo'] == ''
