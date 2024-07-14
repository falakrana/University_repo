# Sorting the Sentence


def sortSentence(s):
    words = s.split()
    n = len(words)
    original_sentence = [""]*n


    for word in words:
        # This line will comprehend the position of word.
        position = int(word[-1])
        # The line will state the actual word.
        actual_word = word[:-1]
        # Placeing actual word in its correct position
        original_sentence[position - 1] = actual_word

    # Forming the sentence.
    answer_sentence = ""
    for i in original_sentence:
        answer_sentence += i + " "
        
    """
    or:
    answer_sentence = " ".join(original_sentence)
    """

    return answer_sentence


# Example usage:
Jumbles_sentence = "is2 sentence4 This1 a3"
print(sortSentence(Jumbles_sentence))  
