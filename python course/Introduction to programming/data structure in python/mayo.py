def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powel', 'V'],

[3, 'Brian Howel', 'VI'], [4, 'Lynne Foster', 'VI'],

[5, 'Zackary Simon', 'VII']]

print('\nOriginal list of lists:')

print(students)

print('\nConverted lists to a dictionary:')

print(test(students))