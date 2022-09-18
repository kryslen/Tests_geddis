def main():
    file_read = open('cycle_script_612.txt', 'r')
    for line in file_read:
        new_line = int(line)
        print(new_line)
    file_read.close()
        
