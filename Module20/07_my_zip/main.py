def shorts_range(string, tpl):
    return min(len(string), len(tpl))


syms_str = 'abc'
nums_tupl = (10, 20, 30, 40)

pairs = ((syms_str[i_elem], nums_tupl[i_elem])
        for i_elem in range(shorts_range(syms_str, nums_tupl)))

print(pairs)
for i_elem in pairs:
    print(i_elem)