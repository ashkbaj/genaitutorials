# 1. String Concatenation

name = "Ashish"
greeting = "Morning"

print("Hi "+ name +"!, Good "+greeting+".")


# 2. Modulo Operator for better readability

print("Hi %s!, Good %s." % (name, greeting))


# String Interpolation and String formatting are different in python but people confuse these two concepts as same.
# 3. String formatting using str.format() which support "string formatting mini language"
print("Hi {}!, Good {}.".format(name, greeting))

# String formatting with multiple manipulation
print("Hi {a}!, Good {b}".format(a=name, b=greeting))

#4. String formatting using several string literals i.e. f strings
print(f"Hi {name}!, Good {greeting}.")

#Arthimatic inline with f-strings
a = 2
b = 5
c = 10
d = 4

print(f"Calulation inline : {a} * {c} / {b} + {d} = {int(2*10/5+4)}")

# String manipulation using templates

from string import Template

n = Template("Hi $customername!, Good $greet")
print(n.substitute(customername = name, greet = greeting))


# 5.
