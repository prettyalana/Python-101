# Tip Calculator
# TODO: Make this DRY

# bill_total and rating are parameters (placeholders/variables)
# bill_total and rating performs the calculations and are passed in when the function is called
def tip_calculator(bill_total, rating) :
    bill_total = float(bill_total)
    rating = rating.lower()

    good_rating = (20 / 100) * bill_total
    fair_rating = (15 / 100) * bill_total
    bad_rating = (10 / 100) * bill_total
   
    if rating == "good" :
        total_amount = float(bill_total + good_rating)
        # :.2f ensures that the the number is displayed as a floating-point with two decimal places and round up if necessary
        print(f"Tip amount: ${good_rating:.2f}")
        print(f"Your total is ${total_amount:.2f}")
    elif rating == "fair" :
        total_amount = float(bill_total + fair_rating)
        print(f"Tip amount: ${fair_rating:.2f}")
        print(f"Your total is ${total_amount:.2f}")
    else :
        total_amount = float(bill_total + bad_rating)
        print(f"Tip amount: ${bad_rating:.2f}")
        print(f"Your total is ${total_amount:.2f}")
        
# These inputs are arguments because they are actual values         
bill_total_input = input("Bill total: ")        
rating_input = input("How was your service: Good, Bad, or Fair? ")       
        
tip_calculator(bill_total_input, rating_input)
