import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")


def count_meaningful_words(sentence):
    words = word_tokenize(sentence)
    print("debug--- words : ", words)
    return len(words)


# korean_sentence = "나는 학교에 간다"
# english_sentence = "I go to school"

# korean_count = count_meaningful_words(korean_sentence)
# english_count = count_meaningful_words(english_sentence)

# print(f"Korean sentence: {korean_sentence} - Meaningful words: {korean_count}")
# print(f"English sentence: {english_sentence} - Meaningful words: {english_count}")
