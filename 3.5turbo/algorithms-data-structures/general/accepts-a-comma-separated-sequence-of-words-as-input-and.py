def process_words(words):
    # Convert the comma-separated string into a list of words
    word_list = words.split(',')

    # Remove leading and trailing whitespaces from each word
    cleaned_words = [word.strip() for word in word_list]

    # Convert the words to uppercase
    uppercased_words = [word.upper() for word in cleaned_words]

    # Sort the words in alphabetical order
    sorted_words = sorted(uppercased_words)

    # Join the words back into a comma-separated string
    result = ', '.join(sorted_words)

    return result


if __name__ == "__main__":
    # Ask the user to enter a comma-separated sequence of words
    words_input = input("Enter a comma-separated sequence of words: ")

    # Process the words and print the result
    processed_result = process_words(words_input)
    print("Processed result:", processed_result)
