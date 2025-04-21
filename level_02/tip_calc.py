# Tip Calculator

def get_user_inputs():
    bill_amount = float(input("Bill total: "))
    rating = input("How was your service: Good, Bad, or Fair? ")
    return bill_amount, rating


def tip_calculation(bill_amount, rating):
    good_rating = (20 / 100) * bill_amount
    fair_rating = (15 / 100) * bill_amount
    bad_rating = (10 / 100) * bill_amount
    # automatically add a 5% tip
    invalid_rating = (5 / 100) * bill_amount

    if rating == "good":
        return good_rating
    elif rating == "fair":
        return fair_rating
    elif rating == "bad":
        return bad_rating
    else:
        print("Invalid input.")
        return invalid_rating

def total_calculation(bill_amount, tip_amount):
    total_amount = bill_amount + tip_amount
    return tip_amount, total_amount


if __name__ == "__main__":
    bill_amount, rating = get_user_inputs()

    tip_amount = tip_calculation(bill_amount, rating)
    tip_amount, total_amount = total_calculation(bill_amount, tip_amount)

    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total amount: ${total_amount:.2f}")
