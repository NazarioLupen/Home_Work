# multiples_of_3_or_5

def solution (number):
    my_list = list (range(1,number))
    list_of_multiples = []
    for i in my_list:
        if i%3 == 0 or i%5==0:
            list_of_multiples.append (i)
    return sum(list_of_multiples)
            
# solution (10)
