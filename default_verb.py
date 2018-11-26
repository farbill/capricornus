import json
from os import listdir
from os.path import isfile, join

def get_display_dict(verb, noun):
    return {
        "commands": [verb + ' ' + noun],
        "response_type": "display",
        "response": get_default_display_action(verb, noun)
    }

def get_default_display_action(verb, noun):
    if verb == 'talk':
        return 'the {} certainly does not want to talk to you right now'.format(noun)
    elif verb =='eat':
        return 'I just gave up {} last week'.format(noun)
    elif verb == 'view':
        return 'Ahh, what a gorgeous {}'.format(noun)
    elif verb == 'move':
        return 'You can\'t move a {}'.format(noun)
    elif verb == 'climb':
        return 'Stop trying to climb on the {}'.format(noun)
    elif verb == 'feed':
        return "the {} is not hungry right now".format(noun)
    elif verb == 'hit':
        return "Ouch, the {} hit you first".format(noun)
    elif verb == 'lift':
        return "Lifting a {} is no job for you".format(noun)
    elif verb == 'take':
        return "you cant take the {}".format(noun)
    elif verb == 'use':
        return "The {} is not usable".format(noun)
    elif verb == 'enter':
        return "You can't just enter a {}".format(noun)
    elif verb == 'swim':
        return "You can't just swim in a {}".format(noun)


if __name__ == '__main__':
    mypath = '/Users/williamfargo/etc/items/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    verbs = ['swim', 'enter']
    for file in onlyfiles:
        with open(mypath + file, 'r') as f:
            d = json.load(f)
        item_name = file.replace('.json', '')
        without_us = item_name.replace('_', ' ')
        for verb in verbs:
            print(get_default_display_action(verb, without_us))
            action_path = mypath + 'actions/'
            action_filename = verb + '_' + file
            afp = action_path + action_filename
            '''
            with open(afp, 'w') as fo:
                json.dump(get_display_dict(verb, without_us), fo)
            '''
            if 'actions' in d.keys():
                if afp in d['actions']:
                    print('file already exists')
                else:
                    d['actions'].append(afp)
            else:
                d['actions'] = [afp]
        with open(mypath + file, 'w') as outer:
            json.dump(d, outer)




        print(item_name)
        print(d)
