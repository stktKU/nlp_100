import re
import numpy as np

def str2ngram(target, n, n_gram_type='word'):
    # target is string or list
    # type : 'word': returns word n-gram
    #          : 'char': returns character n-gram
    n_gram_list = []
    if n_gram_type=='word':
        symbols_regex = re.compile('[!-/:-@[-`{-~]')
        target = target.rstrip()
        target = symbols_regex.sub('', target)
        target_word_list = target.split()
        if len(target)>=n:
            for i in range(len(target_word_list)-n+1):
                n_gram_list.append('-'.join(target_word_list[i:i+n]))
            n_gram_list = list(set(n_gram_list))
            return n_gram_list
        else:
            return None

    elif n_gram_type=='char':
        symbols_regex = re.compile('[!-/:-@[-`{-~]')
        target = target.rstrip()
        target = symbols_regex.sub('', target)
        if len(target)>=n:
            for i in range(len(target)-n+1):
                n_gram_list.append(target[i:i+n])
            n_gram_list = list(set(n_gram_list))
            return n_gram_list
        else:
            return None
    else:
        print('type must be "word" or "char".')

def string2ngram(target, n, n_gram_type='word'):
    target = ' '.join(target)
    n_gram_list = str2ngram(target)
    return n_gram_list

def shuffle_string(target):
    if len(target)<=4:
        return target
    else:
        sort_index = [i+1 for i in range(len(target)-2)]
        np.random.shuffle(sort_index)
        sort_index = [0] + sort_index + [len(target)-1]
        output = [target[i] for i in sort_index]
        return ''.join(output)
def shuffle_sentence(target):
    target_list = target.split()
    output = [shuffle_string(target_) for target_ in target_list]
    return ' '.join(output)

def cipher(target):
    output = ''
    for target_ in target:
        if target_.islower():
            output+=chr(219-ord(target_))
        else:
            output+=target_
    return output