def no_dups(s):
    # Your code here
    if s == "":
        return ""
    new_string = []
    split_string = s.split(' ')
    for word in split_string:
        if word not in new_string:
            new_string.append(word)
    
    sep = " "
    final_string = sep.join(new_string)
    print("This is final string: ", final_string)
    return final_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))