#!/usr/bin/env python3
# Author ID: [mvaseghi1]

# Opens a file, reads the entire content as a string, and returns it
def read_file_string(file_name):
    with open(file_name,'r') as f:
        return f.read()


def read_file_list(file_name):
 # Opens a file, reads the content line by line into a list, strips new-line characters, and returns the list
    with open(file_name,'r') as f:
        return[line.strip()for line in f]

def append_file_string(file_name, string_of_lines):
# Opens a file in append mode, appends a string to the end of the file, and closes the file
    with open(file_name, 'a') as f:
        f.write(string_of_lines)


def write_file_list(file_name, list_of_lines):
# Opens a file in write mode, writes each item from a list to the file, each on a new line, and closes the file
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')


def copy_file_add_line_numbers(file_name_read, file_name_write):
        # Opens a file for reading, reads all lines into a list
    with open(file_name_read, 'r') as f_read:
        lines = f_read.readlines()
    with open(file_name_write, 'w') as f_write:
    # Opens another file for writing, writes each line from the list prefixed with a line number, and closes the file
        line_number = 1
        for line in lines:
            f_write.write(str(line_number) + ':' + line)
            line_number = line_number + 1 


if __name__ == '__main__':
    # File names
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    
    # Strings and lists to write to files
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    # Append string1 to file1 and print the content of file1
    append_file_string(file1, string1)
    print(read_file_string(file1))
    
    # Write list1 to file2 and print the content of file2
    write_file_list(file2, list1)
    print(read_file_string(file2))
    
    # Copy content of file2 to file3 with line numbers and print the content of file3
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))