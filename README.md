# Word Counter & Text Analyzer (PS 14)

**University:** Rungta International Skills University
**School:** School of Information Technology
**Course:** Bachelor of Computer Application (BCA)
**Language:** Python 3
**Concepts:** Strings, Dictionaries, Sets, Frequency Analysis

## Problem Statement

Build a tool that analyses a piece of text or a text file and reports the number of words, characters, sentences and the frequency of each word.

**Note:** Counting is case-insensitive and punctuation is removed before counting words.

## Features

- Read text typed by the user or from a text file
- Count words, characters (with spaces) and sentences
- Clean text using string methods (`lower`, `split`, `strip`, `replace`)
- Count word frequency using a dictionary
- Find unique words using a set
- Show results sorted by frequency
- Handle invalid input (empty text, file not found)

## Project Structure

```
word_counter.py   # complete solution (single file)
README.md         # documentation
```

## How to Run

1. Install Python 3.
2. Open a terminal / console in the project folder.
3. Run:

```
python word_counter.py
```

4. Choose an option from the menu:

```
1. Analyse text (words, characters, sentences)
2. Frequency (top words & unique words)
3. Exit
```

5. Choose the input source: type text (1) or read from a file (2).

## How It Works

| Function | Purpose |
|---|---|
| `read_text_from_user()` | Takes text typed by the user |
| `read_text_from_file()` | Reads a file; returns `None` if not found |
| `clean_text()` | Lowercases, strips and removes punctuation |
| `get_words()` | Returns the list of clean words |
| `count_sentences()` | Counts sentences ending with `.`, `!` or `?` |
| `word_frequency()` | Builds a dictionary of word counts |
| `sort_by_frequency()` | Sorts by count (high to low), then alphabetically |
| `show_basic_stats()` | Prints words, characters, sentences, unique words |
| `show_frequency()` | Prints top words, unique words and full frequency table |

## Test Cases

| # | Scenario | Input | Expected Output |
|---|---|---|---|
| 1 | Normal input | `Python is easy. Python is fun.` | Words: 6, Characters (with spaces): 30, Sentences: 2 |
| 2 | Boundary / minimum | `Hello` | Words: 1, Characters: 5, Sentences: 1, Unique words: 1 |
| 3a | Invalid: empty text | (empty) | No text to analyse. |
| 3b | Invalid: missing file | `notes.txt` (does not exist) | File 'notes.txt' not found. |
| 4 | Different valid scenario | `The cat saw the dog. The dog ran.` (option 2) | Top words: the: 3 \| dog: 2, Unique words: 5 (cat, dog, ran, saw, the) |

All 4 test cases pass.

## Sample Output

```
--- Text Analysis ---
Words: 6 | Characters (with spaces): 30 | Sentences: 2 | Unique words: 4
```

```
--- Word Frequency ---
Top words: the: 3 | dog: 2
Unique words: 5 (cat, dog, ran, saw, the)
```

## Author

Name: Gautam kumar