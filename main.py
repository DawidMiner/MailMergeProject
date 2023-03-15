letter_pattern = open('Input/Letters/starting_letter.txt')
list_of_lines = letter_pattern.readlines()
names = open('Input/Names/invited_names.txt')
list_of_names = names.readlines()
names_ready_to_print = []
for name in list_of_names:
    name_ready = name.strip('\n')
    names_ready_to_print.append(name_ready)
ready_letter = []
edited_lines = []

for name in names_ready_to_print:
    edited = list_of_lines[0].replace('[name]', name)
    edited_lines.append(edited)

for line in edited_lines:
    list_of_lines[0] = line
    print(letter_pattern)
print(names_ready_to_print)
position = 0
for name in names_ready_to_print:
    full_letter = edited_lines[position]
    position += 1
    new_letter = open(f'Output/ReadyToSend/letter_for_{name}.txt', 'w')
    for letters in range(1, len(list_of_lines)):
        print(name)
        print(list_of_lines[0])
        full_letter += list_of_lines[letters]
        print(full_letter)
    print(full_letter)
    new_letter.write(full_letter)
