def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    # print(file_content)

    def word_count():
        words = file_content.split()
        # print(len(words))
    word_count()

    def char_count():
        chars_count = {}
        chars = list(file_content)
        for char in chars:
            char_lower = char.lower()
            if chars_count.get(char_lower) == None:
                chars_count[char_lower] = 1
            else:
                chars_count[char_lower] = chars_count.get(char_lower) + 1
        print(chars_count)
    char_count()
main()