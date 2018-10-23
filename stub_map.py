import characters
import city


def get_map_stub():
    city_hall = city.District(city.DistrictId(2, 3),
                              "City Hall",
                              ["an item - key1"],
                              ["a clue - the eagle has landed1"],
                              [],  # character list
                              "City Hall short description",
                              "City Hall long description",
                              city.DistrictExits("Dayton Dr",
                                                 "Fallbrook Way",
                                                 "Summer Ln",
                                                 "Shore Blvd"))
    hawkins = city.District(city.DistrictId(2, 4),
                            "Hawkins",
                            ["an item - key2"],
                            ["a clue - the eagle has landed2"],
                            [],  # character list
                            "Hawkins short description",
                            "Hawkins long description",
                            city.DistrictExits("",
                                                 "",
                                                 "",
                                                 ""))
    greenland_grove = city.District(city.DistrictId(1, 3),
                                    "Greenland Grove",
                                    ["an item - key3"],
                                    ["a clue - the eagle has landed3"],
                                    [],  # character list
                                    "Greenland Grove short description",
                                    "Greenland Grove long description",
                                    city.DistrictExits("",
                                                         "",
                                                         "",
                                                         ""))
    oak_square = city.District(city.DistrictId(3, 3),
                               "Oak Square",
                               ["an item - key4"],
                               ["a clue - the eagle has landed4"],
                               [],  # character list
                               "Oak Square short description",
                               "Oak Square long description",
                                city.DistrictExits("",
                                                     "",
                                                     "",
                                                     ""))

    bayrock = city.District(city.DistrictId(0, 3),
                               "Bayrock",
                               [],
                               [],
                               [],  # character list
                               "Bayrock short description",
                               "Bayrock long description",
                                city.DistrictExits("",
                                                     "",
                                                     "",
                                                     ""))

    river_gardens = city.District(city.DistrictId(2, 5),
                               "River Gardens",
                               [],
                               [],
                               [],  # character list
                               "River Gardens short description",
                               "River Gardens long description",
                                city.DistrictExits("",
                                                     "",
                                                     "",
                                                     ""))

    paradise_creek = city.District(city.DistrictId(4, 4),
                               "Paradise Creek",
                               [],
                               [],
                               [],  # character list
                               "Paradise Creek short description",
                               "Paradise Creek long description",
                                city.DistrictExits("",
                                                     "",
                                                     "",
                                                     ""))

    northtown = city.District(city.DistrictId(4, 3),
                               "Northtown",
                               [],
                               [],
                               [],  # character list
                               "Northtown short description",
                               "Northtown long description",
                                city.DistrictExits("",
                                                     "",
                                                     "",
                                                     ""))

    lake_cypress = city.District(city.DistrictId(4, 2),
                               "Lake Cypress",
                               [],
                               [],
                               [],  # character list
                               "Lake Cypress short description",
                               "Lake Cypress long description",
                                city.DistrictExits("",
                                                     "",
                                                     "",
                                                     ""))

    sunset_hills = city.District(city.DistrictId(3, 2),
                               "Sunset Hills",
                               [],
                               [],
                               [],  # character list
                               "Sunset Hills short description",
                               "Sunset Hills long description",
                                city.DistrictExits("",
                                                     "",
                                                     "",
                                                     ""))

    # Hyoung's portion:
    washington_heights = city.District(city.DistrictId(1, 2),
                                       "Washington Heights",
                                       ["an item - key5"],
                                       ["a clue - the eagle has landed5"],
                                       [],  # character list
                                       "Washington Heights short description",
                                       "Washington Heights long description",
                                        city.DistrictExits("",
                                                             "",
                                                             "",
                                                             ""))
    gato_springs = city.District(city.DistrictId(1, 1),
                                 "Gato Springs",
                                 ["an item - key6"],
                                 ["a clue - the eagle has landed6"],
                                 [],  # character list
                                 "Gato Springs short description",
                                 "Gato Springs long description",
                                city.DistrictExits("",
                                                     "",
                                                     "",
                                                     ""))
    webster_mountain = city.District(city.DistrictId(2, 1),
                                     "Webster Mountain",
                                     ["an item - key7"],
                                     ["a clue - the eagle has landed7"],
                                     [],  # character list
                                     "Webster Mountain short description",
                                     "Webster Mountain long description",
                                    city.DistrictExits("",
                                                         "",
                                                         "",
                                                         ""))
    lemon_field = city.District(city.DistrictId(3, 1),
                                "Lemon Field",
                                ["an item - key8"],
                                ["a clue - the eagle has landed8"],
                                [],  # character list
                                "Lemon Field short description",
                                "Lemon Field long description",
                                city.DistrictExits("",
                                                     "",
                                                     "",
                                                     ""))
    colt_wood = city.District(city.DistrictId(3, 0),
                              "Coltwood",
                              ["an item - key9"],
                              ["a clue - the eagle has landed9"],
                              [],  # character list
                              "Coltwood short description",
                              "Coltwood long description",
                                city.DistrictExits("",
                                                     "",
                                                     "",
                                                     ""))
    map_arr = [city_hall, hawkins, greenland_grove, bayrock, river_gardens,
               oak_square, paradise_creek, northtown, lake_cypress, sunset_hills,
               washington_heights, gato_springs, webster_mountain, lemon_field, colt_wood]

    return map_arr