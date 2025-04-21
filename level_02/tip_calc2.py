# tip_calc2.py

from tip_calc import get_user_inputs, tip_calculation

def extended_tip_calculator():
    bill_total, rating = get_user_inputs()
    
    bill_total = float(bill_total)

    party_number = int(input("Split how many ways? "))

    tip_amount = tip_calculation(bill_total, rating)

    total_amount = bill_total + tip_amount

    total_per_person = total_amount / party_number

    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total amount: ${total_amount:.2f}")
    print(f"Amount per person: ${total_per_person:.2f}")

extended_tip_calculator()
