import json


def replace(l, find, replace):
    return [x  if  not (x == find)  else  replace for x in l]



def add_whitepace(s: str) -> str:
    return s + ' '




def add_whitespace_dict_list(dl: dict) -> dict:
    return {add_whitepace(k): map(add_whitepace, v) for k, v in dl.items()}


class NLP(object):
    def __init__(self):
        with open('etc/nlp/prepositions.json', 'r') as f:
            self.prepositions = set(json.load(f)['prepositions'])
            #self.prepositions = list(map(add_whitepace, self.prepositions))

        with open('etc/nlp/verbs.json', 'r') as f:
            self.verbs = json.load(f)
            #self.verbs = add_whitespace_dict_list(self.verbs)

        with open('etc/nlp/nouns.json', 'r') as f:
            self.nouns = json.load(f)
            #self.nouns = add_whitespace_dict_list(self.nouns)


    def translate(self, command):
        command = " ".join(command.split()).split(' ')
        print(command)

        for preposition in self.prepositions:
            command = replace(command, preposition, '')


        for base_verb, synonyms in self.verbs.items():
            for synonym in synonyms:
                command = replace(command, synonym, base_verb)

        for base_noun, synonyms in self.nouns.items():
            for synonym in synonyms:
                command = replace(command, synonym, base_noun)
        command = " ".join(command)
        command = " ".join(command.split())
        #remove whitespace https://stackoverflow.com/questions/1546226/simple-way-to-remove-multiple-spaces-in-a-string

        return command

    def get_jaccard_sim(self, str1, str2):
        # https://towardsdatascience.com/overview-of-text-similarity-metrics-3397c4601f50
        a = set(str1.split())
        b = set(str2.split())
        c = a.intersection(b)
        return float(len(c)) / (len(a) + len(b) - len(c))

    def get_suggestions(self, command, possible_commands, threshold = 0.8):
        suggestions = []
        for possible_command in possible_commands:
            score = self.get_jaccard_sim(command, possible_command)
            if score > threshold:
                suggestions.append(possible_command)
        return suggestions