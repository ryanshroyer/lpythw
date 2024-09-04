from sys import argv

# define the input file we're working with
input_file = "ex20_test.txt"

# create function that takes argument `f`
def print_all(f):
# take file `f` and read it, then print it
	print(f.read())

# create function that takes argument `f`
def rewind(f):
# take `f` and go to the beginning, or "zero byte" of that file
	f.seek(0)

# create function that takes two arguments
def print_a_line(line_count, f):
# read `f` until you reach the first \n break; then print the line count variable and the line
# the end="" argument is used to prevent the print function from adding a newline character
	print(line_count, f.readline(), end="")

# define the variable current file as the open input file
current_file = open(input_file)

# print the string
print("First let's print the whole file:\n")

# print the entire current file
print_all(current_file)

# print the string
print("Now let's rewind, kind of like a tape.")

# call the function rewind, which uses .seek(0) method to go to the beginning of the file, on the current file
rewind(current_file)

# print the string
print("Let's print three lines:")

# define a new variable called current_line and set it to 1
current_line = 1
# call the function, passing its two arguments
print_a_line(current_line, current_file)

# increment the current_line variable by 1
current_line += 1
# call the function, passing its two arguments
print_a_line(current_line, current_file)

# increment the current_line variable by 1
current_line += 1
# call the function, passing its two arguments
print_a_line(current_line, current_file)
