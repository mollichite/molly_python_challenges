def reverse_string(s): 
    return s[::-1]
print(reverse_string("disco ball"))


def third_letter(x):
    return x[3:]
print(third_letter('ball'))

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
print(reverse_string("disco ball"))