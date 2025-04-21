# Tip Calculator
# TODO: Make this DRY

def tip_calculator() :
    bill_total = input("Bill total: ")
    bill_total = float(bill_total)
    rating = input(" How was your service: Good, Bad, or Fair? ")
    rating = rating.lower()

    good_rating = (20 / 100) * bill_total
    fair_rating = (15 / 100) * bill_total
    bad_rating = (10 / 100) * bill_total

        
    if rating == "good" :
        total_amount = float(bill_total + good_rating)
        # :.2f ensures that the the number is displayed as a floating-point with two decimal places and round up if necessary
        print(f"${good_rating:.2f}")
        print(f"Your total is ${total_amount:.2f}")
    elif rating == "fair" :
        total_amount = float(bill_total + fair_rating)
        print(f"${fair_rating:.2f}")
        print(f"Your total is ${total_amount:.2f}")
    else :
        total_amount = float(bill_total + bad_rating)
        print(f"${bad_rating:.2f}")
        print(f"Your total is ${total_amount:.2f}")
tip_calculator()