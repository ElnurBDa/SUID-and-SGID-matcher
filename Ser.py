with open('gtfobins suid.txt', 'r') as list_file:
    commands = set(line.strip() for line in list_file)

with open('found suids.txt', 'r') as found_file:
    for line in found_file:
        words = line.strip().split('/')
        last_word = words[-1]
        if last_word in commands:
            print(line.strip())
