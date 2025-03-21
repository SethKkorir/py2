def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price

if __name__ == "__main__":
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(price, discount_percent)

        print(f"Final price after discount: {final_price:.2f}")
    except ValueError:
        print("Invalid input! Please enter numerical values for price and discount percentage.")
