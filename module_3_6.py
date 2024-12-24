def calculate_structure_sum(*args):
    res = 0
    for x in args:
        if isinstance(x, str):
            res += len(x)
        elif isinstance(x, int) or isinstance(x, float):
            res += x
        elif isinstance(x, dict):
            for k, v in x.items():
                res += calculate_structure_sum(k)
                res += calculate_structure_sum(v)
        #elif isinstance(x, tuple) or isinstance(x, set) or isinstance(x, list) :
        else:
            for v in x:
                res += calculate_structure_sum(v)
    return res


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)