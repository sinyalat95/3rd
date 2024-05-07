"""
Upper and Lower
"""
# Provide your solution here
def count_upper_lower(word) -> None:
    for i in word:
        i.isupper()

    print(f"No. of Upper case characters: ", {count_upper_lower(word)})
    print(f"No. of Lower case characters: ", {count_upper_lower(word)})
"""
Check 33
"""
# Provide your solution here

def has_33(my_list) -> bool:
    for i in my_list:
        if my_list[i] == 3:
            return bool
        print(has_33)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different "
          "scenarios.")
my_list = [1, 5, 5, 3, 5, 4]
print(has_33(my_list))