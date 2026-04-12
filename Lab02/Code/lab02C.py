def find_reverse_pair(word_list):
    reverse_pair_list = []
    
    for x in word_list:
        if ''.join(reversed(x)) in word_list:
            if reverse_pair_list.count(x)!=1:
                reverse_pair_list.append(x)
                reverse_pair_list.append(''.join(reversed(x)))
                if x == ''.join(reversed(x)):
                    reverse_pair_list.remove(x)
                    reverse_pair_list.remove(''.join(reversed(x)))
            
    return reverse_pair_list
