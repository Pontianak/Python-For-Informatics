# Copyright (c) 2015 Pontianak

"""
Prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
"""
try:
    Score = float(raw_input("Enter Score between 0.0 and 1.0: "))
except:
    print "That isn't a valid number!"
    quit()

if Score < 0.6:
    print "F"
elif Score > 1.0:
    print "Error, Number Entered Is To High"
elif Score >= 0.9:
    print "A"
elif Score >= 0.8:
    print "B"
elif Score >= 0.7:
    print "C"
elif Score >= 0.6:
    print "D"
