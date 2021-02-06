
smmry.com - Maybe uses Stanford nlp module to process words, then tf-idf algo to find key phrases - term frequency - inverse document frequency analyzes word count, the more frequent the word, the more importanat (but normalize with the inverse you get from a body of documents, to control for conjunctions etc.) probably easy/fast to implement


###### The core algorithm summarizes in 7 simple steps:
1) Associate words with their grammatical counterparts. (e.g. "city" and "cities")
2) Calculate the occurrence of each word in the text.
3) Assign each word with points depending on their popularity.
4) Detect which periods represent the end of a sentence. (e.g "Mr." does not).
5) Split up the text into individual sentences.
6) Rank sentences by the sum of their words' points.
7) Return X of the most highly ranked sentences in chronological order.

###### then
• Ranking sentences by importance using the core algorithm.
• Reorganizing the summary to focus on a topic; by selection of a keyword.
• Removing transition phrases.
• Removing unnecessary clauses.
• Removing excessive examples.



