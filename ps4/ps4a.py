# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    masterList = [];
    if not sequence:
        return [""];
    elif len(sequence) == 1:
        return [sequence];
    #elif len(sequence) == 2:
    #    return [sequence, sequence[::-1]];
    else:
        possibilities = get_permutations(sequence[1:]);
        for permutation in possibilities:
            for index in range(len(sequence)):
                masterList.append(permutation[0:index]+sequence[0]+permutation[index:]);
        return masterList;
print(get_permutations("abc"))
print(get_permutations("ab"))
print(get_permutations("bust"))

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

