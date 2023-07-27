import requests

def currency_converter(amount, from_currency, to_currency):
    # Construct the API URL with the source currency
    base_url = f"https://open.er-api.com/v6/latest/{from_currency}"
    
    # Fetch exchange rates data from the API
    response = requests.get(base_url)

    # Check if the API request was successful
    if response.status_code != 200:
        print("Failed to fetch exchange rates. Please check your internet connection.")
        return None

    # Parse the JSON response data
    data = response.json()

    try:
        # Get the rates dictionary from the response data
        rates = data["rates"]
        
        # Check if the target currency exists in the rates dictionary
        if to_currency in rates:
            # Perform the currency conversion
            converted_amount = amount * rates[to_currency]
            return converted_amount
        else:
            print(f"Invalid currency code '{to_currency}'. Please enter a valid currency code.")
            return None
    except KeyError:
        print(f"Invalid currency code '{from_currency}' or failed to fetch exchange rates.")
        return None

def main():
    print("Real-Time Currency Converter")
    print("---------------------------")
    print("Available currencies: USD, EUR, GBP, JPY, INR, BRL, CAD, AUD, CHF, CNY, HKD, SGD")

    while True:
        # Prompt user to enter the amount to convert
        amount = float(input("Enter the amount to convert (or enter 0 to exit): "))
        
        # Check if the user wants to exit the program
        if amount == 0:
            print("Exiting...")
            break

        # Prompt user to enter the source currency and target currency
        from_currency = input("Enter the currency to convert from: ").upper()
        to_currency = input("Enter the currency to convert to: ").upper()

        # Perform the currency conversion and display the result
        converted_amount = currency_converter(amount, from_currency, to_currency)
        if converted_amount is not None:
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
