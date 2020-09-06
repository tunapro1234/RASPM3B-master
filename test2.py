def fun(any_input): 
    return int(any_input) + 1

def fun5(input_array): 
    final = 0
    for input in input_array:
        final += fun(input)
    return final
