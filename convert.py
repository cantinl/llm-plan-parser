import sys
import re

'''
translation_dict = {
    "grasp": "Grasp container {1} with the {0} hand.",
    "leave": "Leave container {1} from {0} hand on the table.",
    "fill-shot": "Fill shot {0} in hand {2} with ingredient {1} from dispenser {4} using hand {3}.",
    "pour-shot-to-clean-shaker": "Pour shot {0} containing ingredient {1} into shaker {2} using hand {3}, from level ",
    "clean-shot": "Clean shot",
    "pour-shot-to-used-shaker": "Pour shot to used shaker",
    "shake": "Shake",
    "pour-shaker-to-shot": "Pour shaker to shot",
    "empty-shaker": "Empty shaker"
}
'''

translation_dict = {
    "pickup": "Pick up object {0}.",
    "putdown": "Put down object {0}.",
    "stack": "Stack object {0} on top of object {1}.",
    "unstack": "Unstack object {0} from object {1}."
}

def convert_to_english(input_file):
    with open(input_file, 'r') as file:
        contents = file.read()

    output = ""
    for line in contents.split('\n'):
        if line.startswith(';'):
            continue
        if line.strip() == "":
            continue

        result = re.match(r"\s*\((.*)\)\s*", line)
        if result is None:
            continue
        line = result.group(1)
        command = line.split()
        if len(command) < 2:
            continue

        action = command[0]
        arguments = command[1:]

        if action in translation_dict:
            output += translation_dict[action].format(*arguments) + "\n"

    return output

# Provide the path to the input file
input_file = sys.argv[1]

english_commands = convert_to_english(input_file)
print(english_commands)
