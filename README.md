# Croatian Stemmer

The original implementation (the hard work) is credited to Nikola Ljubešić and Ivan Pandžić.

Luís Gomes adapted the code for usage as a Python module and refactored the code slightly:

- created function `hr_stem(word)` which returns the stem
- load `rules.txt` and `transformations.txt` independently of the current working directory
- program reads tokenized sentences from stdin and writes stemmed sentences to stdout (line-buffered)


The remainder of this file is adapted from [the webpage where the original code is available](http://nlp.ffzg.hr/resources/tools/stemmer-for-croatian/):


Ivan Pandžić and Nikola Ljubešić have created this simple rule-based stemmer for Croatian which they published under the GNU Lesser General Public License.

This stemmer is actually a refinement / redesign of the stemmer presented in the InFuture 2007 paper titled "Retrieving Information in Croatian: building a simple and effcient rule-based stemmer".

It performs a series of transformations (defined in `transformations.txt`) that take care of morphonological changes and a series of rules (defined in `rules.txt`) that remove the suffixes. The stemmer in general works best on adjectives and nouns since, while working on it, they had information retrieval tasks in mind.

They performed basic evaluation of the stemmer on a lemmatized newspaper corpus as gold standard with a precision of 0.986 and recall of 0.961 (F1 0.973) for adjectives and nouns. On all parts of speech we obtained precision of 0.98 and recall of 0.92 (F1 0.947).


