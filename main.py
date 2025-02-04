def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    # print(file_content)

    def word_count():
        words = file_content.split()
        # print(len(words))
    word_count()

    def sort_on(dict):
        return dict[1]
    
    def char_count():
        chars_count = {}
        chars = list(file_content)
        for char in chars:
            char_lower = char.lower()
            if chars_count.get(char_lower) == None:
                chars_count[char_lower] = 1
            else:
                chars_count[char_lower] = chars_count.get(char_lower) + 1
        char_list = list(chars_count.items())
        char_list.sort(reverse=True, key=sort_on)
        for newchar in char_list:
            if newchar[0].isalpha() == True:
                print(f"the '{newchar}' character was found {newchar[1]} times")
    char_count()
main()