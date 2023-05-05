#!/usr/bin/env python3

import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def load_words(filename):
	with open(filename, 'r', encoding='utf-8') as file:
		words = [line.strip().lower() for line in file]
		
	return words

def filter_words(words):
	filtered_words = []
	
	for word in words:
		if len(word) < 5 or len(word) > 9:
			continue
		
		parsed_word = morph.parse(word)[0]
		if 'NOUN' in parsed_word.tag and 'nomn' in parsed_word.tag:
			filtered_words.append(word)
		elif 'VERB' in parsed_word.tag and '1per' in parsed_word.tag and 'sing' in parsed_word.tag:
			filtered_words.append(word)
			
	
	return filtered_words

def save_filtered_words(filename, words):
	with open(filename, 'w', encoding='utf-8') as file:
		for word in words:
			file.write(word + '\n')
			
def main():
	input_filename  = "./russian-words/russian.txt"
	output_filename = "./russian-words/filtered.txt"
	
	words = load_words(input_filename)
	filtered_words = filter_words(words)
	save_filtered_words(output_filename, filtered_words)
	print("Filtered words saved")
	
if __name__ == "__main__":
	main()