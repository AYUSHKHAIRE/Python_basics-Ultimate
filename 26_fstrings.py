letter = " hey my name is {1} andf i am from {0}"
country = "india"
name = "Ayush"
print(letter.format(country, name))

# fstring
print(f" hey my name is {name} andf i am from {country}")

# decimal
txt = "for only{price:.2f} dollars!"
print(txt.format(price=4.9999999999))
prices = 45.5555
print(f"for only{prices:.2f} dollars!")

# as it is
print(f"wer represent fstrings like this : hey my name is {{name}} andf i am from {{country}}")
