from nlp import NLP
translator = NLP()


def command_parsing(command, allowed_list):
    for i in allowed_list:
        if translator.translate(command) == i:
            return 1

    return 0
