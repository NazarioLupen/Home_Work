# count_of_positives

def count_positives_sum_negatives(arr):
    count_positive = 0
    sum_negative = 0
    if len(arr) == 0 or arr == [0,0]:
        return []
    else:
        for number in arr:
            if number >0:
                count_positive +=1
            elif number <0:
                sum_negative+=number
        return[count_positive,sum_negative]
