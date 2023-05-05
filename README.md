# filter_words.py
### Overview
Processes a list of words based on length and part of speech, utilizing an external library to analyze the data. The processed data is subsequently saved to a separate file.

### Architecture and Modules
- **load_words(filename)**: This function ingests a text file and returns its content as a list.
- **filter_words(words)**: This function leverages an external library to analyze words based on length and part of speech before returning the processed data.
- **save_filtered_words(filename, words)**: This function writes the output of filter_words(words) to file.

---

# worlde
### Overview
Assist in the resolution of the game Wordle, wherein players must determine a word with between five to nine letters based on several clues. Works only with Russian.

### Architecture and Modules
The file contains two functions:
- **load_dictionary(filename, word_length)**: This function reads a text file and generates a filtered list of words, dependent on the specified length of the word.
- **filter_words(words, gray_letters, yellow_letters, green_letters, word_length)**: This function identifies possible word matches based on user input, with green letters in the correct positions, yellow letters in incorrect positions, and gray letters not appearing.


# Example:
```
*Enter desired word size (default is 5, maximum is 9)*: 
*Enter gray letters*: лопухырмт
*Enter yellow letters and incorrect positions (e.g., 'a,1;a,3:4')*: в,1;д,3
*Enter green letters and correct positions (e.g., 'a,1;b,2')*: е,2;к,4;а,5
*Possible words*: ['девка']
```
