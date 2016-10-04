Parts of Speech Tagging using NLTK[1], Brown[2] corpus.

Using Hidden Markov Models, assuming bigram model, we calculate the probability of all possible POS comninations of the sentence being tagged. Then we find the particular POS combination with maximum probability.

The sensentence we use here is 'time flies like an arrow'

We use brown's corpus to calculate all the required conditional probabilities of tags & tokens.

We use logarithm of the probability in order not to lose precision.

Result:
The sequence with highest probability is-

('NN', 'VBZ-HL', 'VB-HL', 'AT-NC', 'NN') - (time, flies, like, an, arrow).

The logarithmic probability is -12.66032791780777.


References:

[1] http://www.nltk.org/
[2] http://clu.uni.no/icame/brown/bcm.html
