import city
from items import Item, ItemType, Action, ActionType
from loaders import DistrictLoader


def get_map_stub():
    city_hall = DistrictLoader.parse_json('etc/districts/city_hall.json')
    hawkins = DistrictLoader.parse_json('etc/districts/hawkins.json')
    greenland_grove = DistrictLoader.parse_json('etc/districts/greenland_grove.json')
    oak_square = DistrictLoader.parse_json('etc/districts/oak_square.json')
    bayrock = DistrictLoader.parse_json('etc/districts/bayrock.json')
    river_gardens = DistrictLoader.parse_json('etc/districts/river_gardens.json')
    paradise_creek = DistrictLoader.parse_json('etc/districts/paradise_creek.json')
    northtown = DistrictLoader.parse_json('etc/districts/northtown.json')
    lake_cypress = DistrictLoader.parse_json('etc/districts/lake_cypress.json')
    sunset_hills = DistrictLoader.parse_json('etc/districts/sunset_hills.json')
    washington_heights = DistrictLoader.parse_json('etc/districts/washington_heights.json')
    gato_springs = DistrictLoader.parse_json('etc/districts/gato_springs.json')
    webster_mountain = DistrictLoader.parse_json('etc/districts/webster_mountain.json')
    lemon_field = DistrictLoader.parse_json('etc/districts/lemon_field.json')
    colt_wood = DistrictLoader.parse_json('etc/districts/colt_wood.json')


    map_arr = [city_hall, hawkins, greenland_grove, bayrock, river_gardens,
               oak_square, paradise_creek, northtown, lake_cypress, sunset_hills,
               washington_heights, gato_springs, webster_mountain, lemon_field, colt_wood]

    map_arr = city.assign_street_name(map_arr)

    return map_arr
