def solve(s):
    for name in s.split():
        s = s.replace(name, name.capitalize())
    return s

print(solve("suraj b v"))