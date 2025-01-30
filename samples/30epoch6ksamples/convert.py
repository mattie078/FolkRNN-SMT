import re

# Regular expression to match lines that start with 'X:' followed by digits
x_pattern = re.compile(r"^X:\d+")

x_counter = 1  # Starting count

with open("input.txt", "r") as infile, \
        open("output.txt", "w") as outfile:
    
    for line in infile:
        if x_pattern.match(line):
            # If the line starts with 'X:'
            new_line = "X:{}\n".format(x_counter)
            outfile.write(new_line)
            x_counter += 1
        else:
            # Write the line as-is
            outfile.write(line)
