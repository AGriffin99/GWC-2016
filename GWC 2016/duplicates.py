'''
find_duplicates takes in two lists and returns a list of all their
duplicate elements. For example, if list_a is [1, 2, 3, 4] and list_b is
[2, 5, 6, 3], find_duplicates should return [2, 3].
'''
dupes=[]
def find_duplicates(list_a, list_b):
    # for element in list_a == element in list_b:
    dupes=[]
    for elements in list_a:
        if elements == elements in list_b:
            dupes.append(elements)
            print(dupes)
            return(dupes)


        else:
            dupes=[]
            print(dupes)

        # if element!= element in list_b:
        #     print(dupes)
'''
The code below will test to see if your find_duplicates method is working!
It will print "passed" each time a test succeeds.
'''

def test_find_duplicates(list_a, list_b, expected_result):
    if(find_duplicates(list_a, list_b) == expected_result):
        print("Passed!")
    else:
        print("Your method isn't quite working as expected.")

test_find_duplicates([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 5, 8, 13])
test_find_duplicates([1, 2, 3], [4, 5, 6], [])
test_find_duplicates([1, 2], [1, 2], [1, 2])
test_find_duplicates([1, 2, 3], [1, 1, 3, 3, 4, 5, 9], [1, 3])
