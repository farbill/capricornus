from loaders import CityLoader, ItemLoader
def get_map_stub():
    map_arr = CityLoader.parse_json('etc/city/new_san_diego.json')

    list_of_legendary_files = ["etc/items/vitality_orb.json",
                         "etc/items/vision_orb.json",
                         "etc/items/strength_orb.json",
                         "etc/items/magic_sword.json"]
    list_of_legendary_items = []
    for file in list_of_legendary_files:
        list_of_legendary_items.append(ItemLoader.parse_json(file))

    return map_arr, list_of_legendary_items
