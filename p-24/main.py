with open("input/names/invited_names.txt", "r") as f:
    names = f.readlines()

with open("input/letters/starting_letter.txt", "r") as f:
    template_letter = f.read()

for name in names:
    with open(f"output/readyToSend/invitation_{name}.txt", "w") as f:
        letter = template_letter.replace("[name]", name.strip())
        f.write(letter)