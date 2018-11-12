from loaders import CityLoader
def get_map_stub():
    map_arr, legendary_items = CityLoader.parse_json('etc/city/new_san_diego.json')
    return map_arr, legendary_items
