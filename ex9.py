days = "Mon Tue Wed Thu Fri Sat Sun"
months = "{} Jan \n Feb \n Mar \n Apr \n May \n Jun \n Jul \n Aug"

space = '\n'

print(f"Here are the days: {days}")
print("Here are the months: ", months.format(space))

print("""
    There's something going on here.
    With the the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.
""")
