import json
import random


"""
    defining all function here to use them in the file individually
"""



def open_file():
    """
    Returning data to use in all functions
    :return:
    """

    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    return data


def parse_command():
    """
    Function to select parse data from given json file
    """
    parse_commands = []
    [parse_commands.append(row.copy()) for row in open_file() if 'function' in row and row['function'] == 'parse']
    print(f"parse_commands: {parse_commands}")
    return parse_commands


def copy_command():
    """
        Function to select copy data from given json file
    """
    copy_commands = []
    [copy_commands.append(row.copy()) for row in open_file() if 'function' in row and row['function'] == 'copy']
    print(f"copy_commands: {copy_commands}")
    return copy_commands


def functional_command():
    """
    Returning two lists contains copy and parsed commands data in a single list
    """
    functional_commands = []
    counter = 0
    for row in parse_command():
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'parse'
        new_row['_counter'] = counter
        functional_commands.append(new_row)
    counter = 0
    for row in copy_command():
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'copy'
        new_row['_counter'] = counter
        functional_commands.append(new_row)
    print(f"functional_commands: {functional_commands}")
    return functional_commands


def random_command():
    """
        getting two random commands from json file
    """
    random_commands = random.sample(open_file(), 2)
    print(f"random_commands: {random_commands}")
    return random_commands


def main() -> (dict, dict, dict, dict, ):

    """
        calling functions for main to used in the code
    """
    parse_commands = parse_command()

    copy_commands = copy_command()

    functional_commands = functional_command()

    random_commands = random_command()

    return parse_commands, copy_commands, functional_commands, random_commands


if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = main()

    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2


    """
        variable based testing here in the file
    """

    # assert parse_commands == 1
    # assert parse_commands == "string"
    # assert parse_commands == (1, 2, 4, 6)
    # assert parse_commands == {1: "value", 2: 'check'}