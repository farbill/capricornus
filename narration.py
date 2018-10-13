def narration(the_string, line_length):
    counter = 0

    to_print = " " * int(line_length / 8)
    last_line_indicator = 0

    for i in the_string:
        to_print += i
        counter += 1
        last_line_indicator += 1

        if counter > (int(line_length * 5 / 8)):
            if i != " ":
                continue
            print(to_print)
            counter = 0
            to_print = " " * int(line_length / 8)

    if last_line_indicator <= len(the_string):
        print(to_print)





