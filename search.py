"""
Search!
"""
from itertools import chain
import re
import string
from os import listdir

# import sys, time

class SearchIndex(object):
    """
    Maintain a search index.
    """
    cleanup_regex = re.compile('([^a-zA-Z]{1,}|\\s{1,}|\\n)')

    document_index = {}
    main_index = {}

    def __init__(self, file_wildcard='.txt'):
        text_files = [tf for tf in listdir('docs', ) if tf.endswith(file_wildcard)]

        for text_file in text_files:
            with open('docs/' + text_file, mode='r') as text_file_content:
                file_content = string.join(text_file_content.readlines())

                current_index = {}

                for pos, word in enumerate(self.cleanup_regex.sub(' ', file_content).lower().split(' ')):
                    if word in current_index:
                        current_index[word].append(pos)
                    else:
                        current_index[word] = [pos]

                self.document_index[text_file] = current_index

        for (doc_key, word_key,) in set(((doc_key, word_key,) for doc_key, doc_val in self.document_index.iteritems() for word_key, _ in doc_val.iteritems())):
            if word_key in self.main_index:
                self.main_index[word_key].append(doc_key)
            else:
                self.main_index[word_key] = [doc_key]

    def search(self, phrase):
        """
        """
        if not phrase.strip():
            return

        split_phrase = phrase.strip().split(' ')

        docs_to_search = list(set(chain(*[self.main_index[search_term] for search_term in split_phrase if self.main_index.has_key(search_term)])))

        # Find documents with all the words in the phrase.
        for doc in docs_to_search:
            if all(search_word in self.document_index[doc] for search_word in split_phrase):
                phrase_found = True

                word_index = self.document_index[doc]

                target_positions = []

                for index, word in enumerate(split_phrase):
                    if target_positions and not any(pos in word_index[word] for pos in target_positions):
                        phrase_found = False
                        break

                    target_positions = [pos + index + 1 for pos in word_index[word]]

                if phrase_found:
                    yield doc

# search_index = SearchIndex()



# def main(*args):
#     """
#     Let's search!
#     """
#     print "hello"
#     begin_init_time = time.time()
#     search = SearchIndex()
#     end_init_time = time.time()

#     total_init_time = end_init_time - begin_init_time

#     print 'Search Initialized in {0} seconds.'.format(total_init_time)

#     begin_search_time = time.time()
#     results = list(search.search('hacker crackdown'))
#     end_search_time = time.time()

#     total_search_time = end_search_time - begin_search_time

#     print results

#     print 'Search completed in {0} seconds.'.format(total_search_time)


# if __name__ == '__main__':
#     main(*sys.argv)
