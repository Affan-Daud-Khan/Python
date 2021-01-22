import string


sentence = input()


def to_jaden_case(sentence):
    splitSentence = sentence.split()
    jadenSentence = '';
    for word in splitSentence:
        capitalizedWord = word.capitalize()
        jadenSentence = jadenSentence + " " + capitalizedWord

    answer = jadenSentence.strip()
    print(answer)

# def to_jaden_case(sentence):
#     print(" ".join(w.capitalize() for w in sentence.split()))

# def to_jaden_case(sentence):
#     print(string.capwords(sentence))

to_jaden_case(sentence)
