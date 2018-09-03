def count_characters(input_str):
    characters = {}
    my_str = input_str.lower()
    for ch in my_str:
        if characters.get(ch):
            characters[ch] += 1
        else:
            characters[ch] = 1

    sort_dict = sorted(characters.items(), key=lambda x:x[1])[::-1]
    result = sort_dict[:3]      

    return result               	



def main():
    input_str = input("Enter string: ")
    print(count_characters(input_str))


if __name__ == "__main__":
    main()
