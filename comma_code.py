# Comma Code
spam = ['apples', 'bananas', 'tofu', 'cats']
print(spam[:-1]) # ['apples', 'bananas', 'tofu']
print(spam[-1]) # cats

def list_to_string(seq):
    if len(seq) <= 2:
        seq_str = ' and '.join(seq)
        print(seq_str)
    else:
        seq_str = f"{', '.join(seq[:-1])} and {seq[-1]}"
        # seq_str = ', '.join(seq[:-1]) + ' and ' + seq[-1]
        print(seq_str)

list_to_string(['apples', 'bananas', 'tofu']) # apples, bananas and tofu