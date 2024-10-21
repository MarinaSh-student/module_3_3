def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(88, 'линия', False)
print_params(47, 'волна')
print_params(b = 25)
print_params(c = [1,2,3])


values_list = (1812, 'Бородино', 7.09)
values_dict = {'a' : 1812,  'b' : 'Бородино', 'c' : 7.09}
print_params (*values_list)
print_params(**values_dict)

values_list = (1812, 'Бородино')
values_dict = {'c' : 7.09}
print_params(*values_list , **values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)