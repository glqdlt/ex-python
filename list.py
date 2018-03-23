cast = ["1item", 2, "3item", ["inner 1", "inner 2", ["in_inner1", "in_inner2", "in_inner3"]]]

# case 1 , not printing inner list..
print("==============")
for item in cast:
    print(item)

# case 2
print("==============")
for item in cast:
    if isinstance(item, list):
        for in_i in item:
            if isinstance(in_i, list):
                for in_in_i in in_i:
                    print(in_in_i)
            else:
                print(in_i)

# case 3 def ..

print("=============")


def print_lol(the_list):
    for in_item in the_list:
        if isinstance(in_item, list):
            print_lol(in_item)
        else:
            print(in_item)


print_lol(cast)
