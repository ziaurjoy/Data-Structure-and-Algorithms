

# def average(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
#
# def test_average():
#     assert 3 == average([1, 2, 3, 4, 5])



# table driven test

def average(l):
    if not l:
        return None
    return sum(l)/len(l)

def test_average():
    test_cases = [
        {
            'Name': 'simple case 1',
            'input': [1, 2, 3],
            'excepted': 2
        },
        {
            'Name': 'simple case 2',
            'input': [1, 2, 3, 4],
            'excepted': 2.5
        },
        {
            'Name': 'list with one item',
            'input': [100],
            'excepted': 100
        },
        {
            'Name': 'Empty list',
            'input': [],
            'excepted': None
        },
    ]

    for test_case in test_cases:
        assert test_case['excepted'] == average(test_case['input']), test_case['Name']