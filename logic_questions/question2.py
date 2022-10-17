test_data = "Hello welcome to Cathay 60th year anniversary"


# include handle white space char
def count_chars(input_str):
    input_str = input_str.upper()
    unique_chars = list(set(input_str))
    return {char: input_str.count(char) for char in unique_chars}


# ignore handle white space char
def count_chars_v2(input_str):
    input_str = input_str.upper().replace(" ", "")
    unique_chars = list(set(input_str))
    return {char: input_str.count(char) for char in unique_chars}


for key, value in count_chars_v2(test_data).items():
    print(f"{key} {value}")
