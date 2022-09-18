def main():
#receive inputs
    score_1 = int(input())
    score_2 = int(input())
    score_3 = int(input())
    score_4 = int(input())
    score_5 = int(input())

#recieve average
    average = calc_average (score_1, score_2, score_3, score_4, score_5)
    print ('Average is ', average)
    
#receive equivalent in letters
        
    range_letter1 = convert_to_letter(score_1)
    range_letter2 = convert_to_letter(score_2)
    range_letter3 = convert_to_letter(score_3)
    range_letter4 = convert_to_letter(score_4)
    range_letter5 = convert_to_letter(score_5)
    print ('Equivalent in letters is ', range_letter1, range_letter2, range_letter3, range_letter4, range_letter5, end = ' ')
        
#average function

def calc_average(a, b, c, d, e):
    result_average = (a+b+c+d+e)/5
    return result_average

#convert to letter function

def convert_to_letter(mark):
    if 90 <= mark <= 100:
        return 'A'
    elif 80 <= mark <= 89:
        return 'B'
    elif 70 <= mark <= 79:
        return 'C'
    elif 60 <= mark <= 69:
        return 'D'
    else:
        return 'E'
