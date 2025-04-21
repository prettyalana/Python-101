# Tip Calculator

def get_user_inputs():
    bill_total = float(input("Bill total: "))
    rating = input("How was your service: Good, Bad, or Fair? ")
    return bill_total, rating


def tip_calculation(bill_total, rating):
    good_rating = (20 / 100) * bill_total
    fair_rating = (15 / 100) * bill_total
    bad_rating = (10 / 100) * bill_total

    if rating == "good":
        return good_rating
    elif rating == "fair":
        return fair_rating
    elif rating == "bad":
        return bad_rating
    else:
        print("Invalid input.")
        
    return tip_amount


def total_calculation(bill_total, tip_amount):
    total_amount = bill_total + tip_amount
    return tip_amount, total_amount


if __name__ == "__main__":
    bill_total, rating = get_user_inputs()

    tip_amount = tip_calculation(bill_total, rating)
    tip_amount, total_amount = total_calculation(bill_total, tip_amount)

    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total amount: ${total_amount:.2f}")
