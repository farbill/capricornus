import json


class NLP(object):
    def __init__(self):
        with open('etc/nlp/prepositions.json', 'r') as f:
            self.prepositions = set(json.load(f)['prepositions'])

        with open('etc/nlp/verbs.json', 'r') as f:
            self.verbs = json.load(f)

        with open('etc/nlp/nouns.json', 'r') as f:
            self.nouns = json.load(f)

    def translate(self, command):
        for base_verb, synonyms in self.verbs.items():
            for synonym in synonyms:
                command = command.replace(synonym, base_verb)

        for base_noun, synonyms in self.nouns:
            for synonym in synonyms:
                command = command.replace(synonym, base_noun)

        for preposition in self.prepositions:
            command = command.replace(preposition, '')

        #remove whitespace https://stackoverflow.com/questions/1546226/simple-way-to-remove-multiple-spaces-in-a-string
        command = " ".join(command.split())
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
