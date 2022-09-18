
def main():
#to create file to writting
    file = open('cycle_script_612.txt', 'w')
    
#to create loop for adding values
    for count in range (1, 11):
        file.write(str(count) + '\n')
    file.close()
    print(count)
