def main():
    file_read = open ('cycle_script_612.txt', 'r')
    line = file_read.readline()
    while line != ' ':
        new_line = float(line)
        print (format(new_line, '.1f'))
        line = file_read.readline()
    file_read.close()
