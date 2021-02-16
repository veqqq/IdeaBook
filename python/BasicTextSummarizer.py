def summarize(input_file, output_num):
    with open("stop_words.txt", "r") as open_file:
        stop_text = open_file.readlines()
    stop_text = [word.strip() for word in stop_text]

    with open(input_file, "r") as open_file:
        input_text = open_file.readlines()
    input_text = break_into_sentences(input_text)

    word_values = {}
    for sentence in input_text:
        words = sentence.split(' ')
        for word in words:
            word = strip(word)
            if not word in stop_text:
                if not word in word_values:
                    word_values[word] = 1
                else:
                    word_values[word] += 1

    sentence_values = []
    for sentence in input_text:
        sentence_value = 0   
        words = sentence.split(' ')
        for word in words:
            sentence_value += word_values.setdefault(word, 0)
        sentence_values.append(sentence_value)

    for ii in range(0, output_num):
        highest_val_ind = sentence_values.index(max(sentence_values))
        print(input_text[highest_val_ind])
        del input_text[highest_val_ind]
        del sentence_values[highest_val_ind]

def break_into_sentences(input_text): 

    with open("acronyms.txt", "r") as open_file:
        acronyms = open_file.readlines()    
    acronyms = [word.strip() for word in acronyms]

    input_text = ''.join(input_text).replace('\n','')

    all_sentences = []
    current_sentence = []
    split_text = input_text.split(' ')
    for ind, word in enumerate(split_text):

        current_sentence.append(word + ' ')

        # TODO: needs acronym checking
        for acronym in acronyms:
            if acronym in word:
                pass

        if '.' in word or '?' in word or '!' in word:

            next_word_cap = False
            if ind != len(split_text) - 1:
                if split_text[ind+1].capitalize() == split_text[ind+1]:
                    next_word_cap = True
            if next_word_cap:
                current_sentence = ''.join(current_sentence)
                all_sentences.append(current_sentence)
                current_sentence = []

    return all_sentences

def strip(word):
    return word.strip().strip(',').strip(':').strip('(').strip(')').lower()


if __name__ == "__main__":
    summarize("input_file2.txt", 1)
