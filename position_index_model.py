# positional_index = {
#   "term": [docfreq, {"docID": [postions]}, {"docID": [postions]}],
#   "term": [docfreq, {"docID": [postions]}, {"docID": [postions]}]
# }
#
import stopwords

def initialize_posting_list(tokens_list):
    posting_list = {}
    for token in tokens_list:
        posting_list[token] = []
    return posting_list


def get_positions_in_doc(term, doc):
    positions = [i + 1 for i, t in enumerate(doc) if t == term]
    return positions


def calc_term_frequency(term, doc):
    return len(get_positions_in_doc(term, doc))


def construct_positional_index(main_dictionary, tokens_list):
    positional_index = initialize_posting_list(tokens_list)
    for term in tokens_list:
        for dictionary in main_dictionary:
            for doc_id, tokens in dictionary.items():
                # check if term is occuring in this doc
                # if it is occuring, get positions and return object {doc_id: [positions]}
                # and append this object to the positional index model corresponding term
                term_positions = get_positions_in_doc(term, tokens)
                if not term_positions:
                    continue
                obj = {doc_id: term_positions}
                positional_index[term].append(obj)
        # get doc frequency by getting length and insert it to the beginning of list
        doc_frequency = len(positional_index[term])
        positional_index[term].insert(0, doc_frequency)
    return positional_index


def difference_between_two_arrays(first_document_positions, second_document_positions):
    # We loop through second list
    for second_doc_index, pos in enumerate(second_document_positions):
        first_doc_length = len(first_document_positions)
        # Check if second list is larger or equal to the first list
        if(len(second_document_positions) >= first_doc_length):
            # Check if item of second
            if(pos > first_document_positions[second_doc_index] and (pos - first_document_positions[second_doc_index] == 1)):
                return True
        else:
            # second list is smaller than first list
            if(first_doc_length != second_doc_index):
                if(pos > first_document_positions[second_doc_index] and (pos - first_document_positions[second_doc_index] == 1)):
                    return True
    return False


# occurrence object = [{doc_id:[positions]}]
def compare_two_term_occurrences(first_term_occurrences, second_term_occurrences):
    result = []
    for first_occurence in first_term_occurrences:
        for first_document_id, first_document_positions in first_occurence.items():
            for second_occurence in second_term_occurrences:
                for second_document_id, second_document_positions in second_occurence.items():
                    if(first_document_id == second_document_id):
                        found = difference_between_two_arrays(first_document_positions, second_document_positions)
                        if(found):
                            result.append(first_document_id)
    return result

# [1,3,5,8]
# [2,6,7]

print(compare_two_term_occurrences(
        [{1:[1,3,6]}, {2:[4, 5, 10, 15]}], 
        [{1:[1, 3, 4, 5]}, {3: [3,4,5,6]}]))
# print(compare_two_term_occurrences([{1:[1,3,6]}], [{1:[1, 4, 5, 6, 7]}]))

# positional_index = {
#   "term": [docfreq, {"docID": [postions]}, {"docID": [postions]}]
# }
# 
# Match found in doc #1
def phrase_query(query, positional_index):
    # tokenize query, remove stopwords
    tokens = query.split(' ')
    tokens = stopwords.extract_stopwords(tokens)
    print(tokens)

    result = []
    # catch first term from query
    # find term and its positions in each doc in positional index
    # get same data for second term,
    # compare positions in each doc for first and second, if difference is 1, add to result
    # else not found in doc
    for index, first_term in enumerate(tokens):
        if(tokens[-1] == first_term):
            return result
        second_term = tokens[index + 1]
        for term_name, documents_array in positional_index.items():
            if(term_name == first_term):
                # continue
                first_term_occurrences = documents_array
            if(term_name == second_term):
                # continue
                second_term_occurrences = documents_array
            
            
            
        
