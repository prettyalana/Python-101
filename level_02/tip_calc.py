# Tip Calculator
# TODO: Make this DRY

bill_total = input("Bill total: ")
bill_total = float(bill_total)
rating = input(" How was your service: Good, Bad, or Fair? ")
rating = rating.lower()

# Visit the key value pairs later
# tip_percentages = {
#     "good": (20 / 100),
#     "fair": (15 / 100),
#     "bad": (10 / 100)
# }

good_rating = (20 / 100) * 100
fair_rating = (15 / 100) * 100
bad_rating = (10 / 100) * 100

    
if rating == "good" :
    total_amount = float(bill_total + good_rating)
    print(f"{good_rating}")
    print(f"Your total is {total_amount}")
elif rating == "fair" :
    total_amount = float(bill_total + fair_rating)
    print(f"{fair_rating}")
    print(f"Your total is {total_amount}")
else :
    total_amount = float(bill_total + bad_rating)
    print(f"{bad_rating}")
    print(f"Your total is {total_amount}")