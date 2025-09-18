#match / case 
#Works like a switch statement in other languages.
#Compares a value against specific patterns or cases.
#Cleaner when you’re checking one variable against many possible values.

#but

#if / elif / else
#Used for conditional logic.
#Checks whether a condition is True or False.
#Can test any kind of condition (comparisons, ranges, logic, etc.)

#and

#Key differences:
#Use if when:
#You need to check ranges (x > 5), multiple conditions (x > 5 and y < 10), or logic.
#The conditions are not just about "equal to something".
#Use match when:
#You are checking one variable against a list of possible fixed values.
#It makes the code shorter and easier to read


#example1
def day_of_week(day):
  if day == 1:             
    return "It is Sunday"
  elif day == 2:
    return "It is Monday"
  elif day == 3:
    return "It is Tuesday"
  elif day == 4:
    return "It is Wednesday"
  elif day == 5:
    return "It is Thursday"
  elif day == 6:
    return "It is Friday"
  elif day == 7:
    return "It is Saturday"
  else:
    return "Not a valid day"

print(day_of_week(1))


#example2
def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a valid day"

# Example test
print(day_of_week(5))   # Output: It is Thursday
print(day_of_week(8))   # Output: Not a valid day


#example3
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":         # | = or
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:                             # | = else
            return False

print(is_weekend("Friday"))

