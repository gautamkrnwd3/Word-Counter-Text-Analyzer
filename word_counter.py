"""
PS 14 - Word Counter & Text Analyzer
Language : Python 3
Concepts : Strings, Dictionaries, Sets, Frequency Analysis
Note     : Counting is case-insensitive and punctuation is removed
           before counting words.
"""

import string


def read_text_from_user():
    """Read text typed by the user."""
    return input("Enter your text: ")


def read_text_from_file(filename):
    """Read text from a file. Returns None if file is not found."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None


def clean_text(text):
    """Lowercase, strip and remove punctuation using string methods."""
    text = text.lower().strip()
    for p in string.punctuation:
        text = text.replace(p, "")
    return text


def get_words(text):
    """Return list of clean words."""
    return clean_text(text).split()


def count_sentences(text):
    """Count sentences ending with . ! or ?"""
    temp = text.replace("!", ".").replace("?", ".")
    parts = temp.split(".")
    count = 0
    for part in parts:
        if part.strip() != "":
            count += 1
    return count


def word_frequency(words):
    """Count frequency of each word using a dictionary."""
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq


def sort_by_frequency(freq):
    """Sort by highest frequency first, then alphabetically."""
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))


def show_basic_stats(text):
    words = get_words(text)
    unique = set(words)
    print("\n--- Text Analysis ---")
    print("Words:", len(words), "| Characters (with spaces):", len(text),
          "| Sentences:", count_sentences(text),
          "| Unique words:", len(unique))


def show_frequency(text):
    words = get_words(text)
    freq = word_frequency(words)
    sorted_freq = sort_by_frequency(freq)

    # Top words = words repeated more than once (else first 5 words)
    top = [item for item in sorted_freq if item[1] > 1]
    if not top:
        top = sorted_freq[:5]
    top_text = " | ".join(w + ": " + str(c) for w, c in top)

    unique = sorted(set(words))
    print("\n--- Word Frequency ---")
    print("Top words:", top_text)
    print("Unique words:", len(unique), "(" + ", ".join(unique) + ")")
    print("\nAll words (sorted by frequency):")
    for w, c in sorted_freq:
        print(" ", w, "->", c)


def get_input_text():
    """Ask the user for the source of text. Returns text or None."""
    print("\nChoose input source:")
    print("1. Type text")
    print("2. Read from file")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        text = read_text_from_user()
    elif choice == "2":
        filename = input("Enter file name: ").strip()
        text = read_text_from_file(filename)
        if text is None:
            print("File '" + filename + "' not found.")
            return None
    else:
        print("Invalid choice.")
        return None

    if text.strip() == "":
        print("No text to analyse.")
        return None
    return text


def main():
    print("=== Word Counter & Text Analyzer ===")
    text = None
    while True:
        print("\nMenu:")
        print("1. Analyse text (words, characters, sentences)")
        print("2. Frequency (top words & unique words)")
        print("3. Exit")
        option = input("Enter option (1/2/3): ").strip()

        if option == "3":
            print("Goodbye!")
            break
        elif option in ("1", "2"):
            text = get_input_text()
            if text is None:
                continue
            if option == "1":
                show_basic_stats(text)
            else:
                show_frequency(text)
        else:
            print("Invalid option. Please choose 1, 2 or 3.")


if __name__ == "__main__":
    main()