# Tip Calculator Cont...

from tip_calc import get_user_inputs, tip_calculation

def extended_tip_calculator():
    bill_amount, rating = get_user_inputs()
    
    bill_amount = float(bill_amount)

    party_number = int(input("Split how many ways? "))

    tip_amount = tip_calculation(bill_amount, rating)

    total_amount = bill_amount + tip_amount

    total_per_person = total_amount / party_number

    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total amount: ${total_amount:.2f}")
    print(f"Amount per person: ${total_per_person:.2f}")

extended_tip_calculator()
