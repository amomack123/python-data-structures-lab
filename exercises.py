def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

def manage_students():
    # your code here
    students = ['Noah', 'Andrew', 'Brian']
    first_student = students[1]
    last_student = students[-1]
    return first_student, last_student

def combine_foods():
    foods = ('burger', 'fried rice', 'salad')
    meal = ''
    for food in foods:
        meal += food + ' '
    return meal

def slice_foods():
    # your code here
    foods = ('burger', 'fried rice', 'salad')
    last_two_foods=foods[-2:]
    return last_two_foods

def hometown_info():
    # your code here
    home_town = {
      'city': 'Los Angeles',
      'state': 'CA',
      'population': 3822000,
    }
    return f'I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']} people.'

def list_home_town_items():
    home_town = {
        'city': 'Noida',
        'state': 'Uttarpradesh',
        'population': 3938283
    }

    home_town_items = []
    
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")
    
    return home_town_items



