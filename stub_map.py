from loaders import CityLoader
def get_map_stub():
    map_arr = CityLoader.parse_json('etc/city/new_san_diego.json')
    return map_arr
