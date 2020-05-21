cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
      (original order)"""
    
    final = ""
    for jeep in cars['Jeep'][:-1]:
      final += (jeep+", ")
    final += cars['Jeep'][-1]
    return final



    
def get_first_model_each_manufacturer(cars=cars):
    """get first model of each manufacturer(original ordering)"""
    
    _list = [cars[k][0] for k in cars]
    return _list

                


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
      'grep' string which defaults to 'trail' for this exercise,
      sort the resulting sequence alphabetically"""
    trail_list =  [model for key_ in cars for model in cars[key_] if grep.lower() in model.lower()]
    trail_list.sort()
    return trail_list
    
    
    
    
def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
      sorted alphabetically"""
    cars_ = cars.copy()
    
    for k in cars:
        cars[k].sort()
    return cars_
   
    