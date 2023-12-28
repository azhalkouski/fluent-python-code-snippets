"""
List comprehensions, generator expressions and their siblings set and dict
comprehensions have their own local scope for variables, like functions.
Variables assigned within the expression are local, but variables in the
surrounding scope can still be referenced.
"""
x = 'my precious'
dummy = [x for x in 'ABC']
print(x == 'my precious')



"""
Cartesian product using a list comprehension
"""
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
                         for size in sizes]
print(tshirts)


# the same as
for color in colors:
    for size in sizes:
        print((color, size))


"""
Cartesian product in a generator expression
"""
for tshirts in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirts)
