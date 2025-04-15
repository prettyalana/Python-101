# Work or Sleep In?
from day_of_week import day_input

day = day_input()

work_days = list(range(1,6))
week_ends = [0, 6]


if day in work_days :
    print("Go to work")
elif day in week_ends :
    print("Stay in")
else :
    print("Invalid input")