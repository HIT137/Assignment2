from transformers import AutoTokenizer
from collections import Counter
import os
from multiprocessing import Pool


 #Reminder:Process took like 30 minutes for me to get the output
 #use different model except bert_uncased
def process_chunk(chunk, tokenizer):
    tokens = tokenizer.tokenize(chunk)
    return Counter(tokens)

def count_unique_tokens_and_top_words(text_file_path, model_name, chunk_size=10000, num_processes=4):
    # Read the text file
    with open(text_file_path, 'r') as file:
        text = file.read()

    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Split text into chunks
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Tokenize each chunk and count tokens
    with Pool(num_processes) as p:
        token_counters = p.starmap(process_chunk, [(chunk, tokenizer) for chunk in chunks])

    # Combine token counters from all chunks
    total_counter = sum(token_counters, Counter())

    # Get the top 30 words
    top_words = total_counter.most_common(30)

    return total_counter, top_words

if __name__ == '__main__':
    # Example usage
    text_file_path = r'C:\Users\kzb19\Desktop\ASSSOFTWARE\TEXT.txt'
    model_name = "google/long-t5-local-base"
    token_counts, top_words = count_unique_tokens_and_top_words(text_file_path, model_name)

    print("Unique Tokens Count:", len(token_counts))
    print("Top 30 Words:")
    for word, count in top_words:
        print(word, ":", count)
