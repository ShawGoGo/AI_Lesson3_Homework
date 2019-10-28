# 实现 print 函数

def print_string(*strs, sep = ' ', end = '\n'):
    string = ''
    if len(strs) == 1:
        strs = 'a'
    for str in strs:
        string += str + sep
    string = string[:-1] + end
    print(string)
    return string

print_string('This is a test')
print_string('This', 'is', 'a', 'test')
print_string('This', 'is', 'a', 'test', sep = '-')
print_string('This', 'is', 'a', 'test', sep = '_',end = '.')
