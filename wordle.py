#!/usr/bin/env python3

def load_dictionary(filename, word_length):
	with open(filename, 'r') as file:
		words = [line.strip().lower() for line in file if len(line.strip()) == word_length]
	
	return words

def filter_words(words, gray_letters, yellow_letters, green_letters, word_length):
	possible_words = []
	
	for word in words:
		if any(c in gray_letters for c in word):
			continue
		
		if not all(c == word[i] for i, c in green_letters.items()):
			continue
		
		if any(c == word[i] for c, indices in yellow_letters.items() for i in indices):
			continue
		
		if any(all(word[i] != c for i in set(range(word_length)) - set(indices)) for c, indices in yellow_letters.items()):
			continue
		
		possible_words.append(word)
		
	return possible_words

# TODO: not working when there is no yellow letters provided

def main():
	filename 	= "./dictionary.txt"
	word_size 	= input("Enter desired word size (default is 5, maximum is 9): ")
	word_length = 5 if word_size == '' else int(word_size)
	
	words = load_dictionary(filename, word_length)
	
	gray_letters = input("Enter gray letters: ").lower()
	
	yellow_input = input("Enter yellow letters and incorrect positions (e.g., 'a,1;a,3:4'): ").lower()
	yellow_letters = {letter: [int(pos) - 1 for pos in positions.split(':')] for item in yellow_input.split(';') for letter, positions in [item.split(',', 1)]} if yellow_input else {}
			
	green_input = input("Enter green letters and correct positions (e.g., 'a,1;b,2'): ").lower()
	green_letters = {int(pos) - 1: letter for item in green_input.split(';') for letter, pos in [item.split(',')]} if green_input else {}
	
	possible_words = filter_words(words, gray_letters, yellow_letters, green_letters, word_length)
	print("Possible words:", possible_words)
	
if __name__ == "__main__":
	main()