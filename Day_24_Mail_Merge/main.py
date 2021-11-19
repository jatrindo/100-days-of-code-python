# File paths
invited_names_path = "Input/Names/invited_names.txt"
starting_letter_path = "Input/Letters/starting_letter.txt"
letter_filename_path_template = "Output/ReadyToSend/letter_for_{name}.txt"

# Read in names
with open(invited_names_path) as f:
    names = f.readlines()

# Read in template
with open(starting_letter_path) as f:
    letter_content = f.read()

# Make a unique letter for each individual name
for name in names:
    name = name.strip()
    letter_filename_path = letter_filename_path_template.replace('{name}', name)
    with open(letter_filename_path, 'w') as f:
        f.write(letter_content.replace('[name]', name))
