import characters
import city
from items import Item, ItemType, Action, ActionType

from typing import List, Dict
import item_instances

def get_map_stub():
    city_hall = city.District(city.DistrictId(2, 3),
                              "City Hall",
                              [
                                  item_instances.statue,
                                  item_instances.lotto_ticket
                              ], # district_items
                              [], # dropped_items
                              [], # clues
                              [],  # character list
                              "City Hall short description --",
                              "City Hall long description --",
                              city.DistrictExits())
    hawkins = city.District(city.DistrictId(2, 4),
                            "Hawkins",
                            [
                                item_instances.magic_sword,
                            ],  # district_items
                            [],  # dropped_items
                            [],  # clues
                            [],  # character list
                            "Hawkins short description",
                            "Hawkins long description",
                            city.DistrictExits())
    greenland_grove = city.District(city.DistrictId(1, 3),
                                    "Greenland Grove",
                                    [],  # district_items
                                    [],  # dropped_items
                                    [],  # clues
                                    [],  # character list
                                    "Greenland Grove short description",
                                    "Greenland Grove long description",
                                    city.DistrictExits())
    oak_square = city.District(city.DistrictId(3, 3),
                               "Oak Square",
                               [],  # district_items
                               [],  # dropped_items
                               [],  # clues
                               [],  # character list
                               "Oak Square short description",
                               "Oak Square long description",
                                city.DistrictExits())

    bayrock = city.District(city.DistrictId(0, 3),
                               "Bayrock",
                                [],  # district_items
                                [],  # dropped_items
                                [],  # clues
                                [],  # character list
                               "Bayrock short description",
                               "Bayrock long description",
                                city.DistrictExits())

    river_gardens = city.District(city.DistrictId(2, 5),
                               "River Gardens",
                                  [],  # district_items
                                  [],  # dropped_items
                                  [],  # clues
                                  [],  # character list
                               "River Gardens short description",
                               "River Gardens long description",
                                city.DistrictExits())

    paradise_creek = city.District(city.DistrictId(4, 4),
                               "Paradise Creek",
                                   [],  # district_items
                                   [],  # dropped_items
                                   [],  # clues
                                   [],  # character list
                               "Paradise Creek short description",
                               "Paradise Creek long description",
                                city.DistrictExits())

    northtown = city.District(city.DistrictId(4, 3),
                               "Northtown",
                              [],  # district_items
                              [],  # dropped_items
                              [],  # clues
                              [],  # character list
                               "Northtown short description",
                               "Northtown long description",
                                city.DistrictExits())

    lake_cypress = city.District(city.DistrictId(4, 2),
                               "Lake Cypress",
                                 [],  # district_items
                                 [],  # dropped_items
                                 [],  # clues
                                 [],  # character list
                               "Lake Cypress short description",
                               "Lake Cypress long description",
                                city.DistrictExits())

    sunset_hills = city.District(city.DistrictId(3, 2),
                               "Sunset Hills",
                                 [],  # district_items
                                 [],  # dropped_items
                                 [],  # clues
                                 [],  # character list
                               "Sunset Hills short description",
                               "Sunset Hills long description",
                                city.DistrictExits())

    # Hyoung's portion:
    washington_heights = city.District(city.DistrictId(1, 2),
                                       "Washington Heights",
                                       [
                                            item_instances.old_siver_coin
                                       ],  # district_items
                                       [],  # dropped_items
                                       [],  # clues
                                       [],  # character list
                                       "Washington Heights is a neighborhood in the middle portion of the New San Diego City.",
                                       "Washington Heights is a neighborhood in the middle portion of the New San Diego City. "\
                                       "The area, with over 150,000 inhabitants as of 2010, is named for Fort Washington.",
                                        city.DistrictExits())
    gato_springs = city.District(city.DistrictId(1, 1),
                                 "Gato Springs",
                                 [
                                    item_instances.vision_orb                                  
                                 ],  # district_items
                                 [],  # dropped_items
                                 [],  # clues
                                 [],  # character list
                                 "Gato Springs is a neighborhood in the south western portion of the New San Diego City.",
                                 "Gato Springs is a neighborhood in the south western portion of the New San Diego City. "\
                                 "It is known for its hot springs, stylish hotels, golf courses and spas.",
                                city.DistrictExits())
    webster_mountain = city.District(city.DistrictId(2, 1),
                                     "Webster Mountain",
                                     [],  # district_items
                                     [],  # dropped_items
                                     [],  # clues
                                     [],  # character list
                                     "Webster Mountain is a neighborhood in the southern portion of the New San Diego City.",
                                     "Webster Mountain is a neighborhood in the southern portion of the New San Diego City. "\
                                     "The mountain, formerly called Notch Mountain, is named after Daniel Webster.",
                                    city.DistrictExits())
    lemon_field = city.District(city.DistrictId(3, 1),
                                "Lemonfield",
                                [],  # district_items
                                [],  # dropped_items
                                [],  # clues
                                [],  # character list
                                "Lemonfield is a neighborhood in the south eastern portion of the New San Diego City.",
                                "Lemonfield is a neighborhood in the south eastern portion of the New San Diego City. "\
                                "A 3,000-pound civic lemon statue sits in the center of Lemonfield.",
                                city.DistrictExits())
    colt_wood = city.District(city.DistrictId(3, 0),
                              "Coltwood",
                              [], # district_items
                              [], # dropped_items
                              [], # clues
                              [],  # character list
                              "Coltwood is a neighborhood in the south eastern portion of the New San Diego City.",
                              "Coltwood is a neighborhood in the south eastern portion of the New San Diego City. "\
                              "The district is well-known for its beautiful forest. ",
                                city.DistrictExits())

    map_arr = [city_hall, hawkins, greenland_grove, bayrock, river_gardens,
               oak_square, paradise_creek, northtown, lake_cypress, sunset_hills,
               washington_heights, gato_springs, webster_mountain, lemon_field, colt_wood]

    map_arr = city.assign_street_name(map_arr)

    return map_arr