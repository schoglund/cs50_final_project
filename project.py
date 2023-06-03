import requests
import config
import json
import sys
import re

API_KEY = config.api_key
accepted_symbols = "USD,GBP,UAH,JPY,INR,ZAR"

def main():
    # starter function to see what symbols are accepted, not to be run in calculator
    hide = True
    if not hide:
        get_accepted_currencies()

    # take out whitespace and comma (if there is one) and make code uppercase (if they use three character code)
    val = input("Value: ")
    val_simplified = simplify(val)

    amount, code = verify_input(val_simplified)

    # convert user input
    convert_to_euros(amount, code)

    # print out Euro value
    #print(f"{val_converted:.2f} EUR")

    


def get_accepted_currencies():
    # setup API
    try:
        response = requests.get("http://api.exchangeratesapi.io/v1/symbols?access_key=" + API_KEY)
    except requests.RequestException:
        sys.exit("Cannot access API.")
    else:
        # if API works, then pull JSON
        try:
            o = response.json()
        except requests.JSONDecodeError:
            sys.exit("Could not read JSON.")
        else:
            print(json.dumps(o, indent=2))


def simplify(user_input: str) -> str:
    return user_input.strip().replace(" ", "").replace(",", "").upper()


def verify_input(user_input: str) -> tuple[float, str]:
    # format 1: '12.34USD' or '12USD'
    if matches := re.search(r"^((?:[0-9]+)(?:\.[0-9]{2})?)([A-Z]{3})$", user_input):
        val_code = matches.group(2)

        if val_code not in accepted_symbols.split(","):
            sys.exit("Currency not accepted.")

        try:
            val_amount = float(matches.group(1))
        except ValueError:
            sys.exit()
        else:
            return val_amount, val_code
            
    # format 2: 'USD12' or 'USD12.34'
    elif matches := re.search(r"^([A-Z]{3})((?:[0-9]+)(?:\.[0-9]{2})?)$", user_input):
        val_code = matches.group(1)

        if val_code not in accepted_symbols.split(","):
            sys.exit("Currency not accepted.")

        try:
            val_amount = float(matches.group(2))
        except ValueError:
            sys.exit()
        else:
            return val_amount, val_code
    
    # format 3: '$12' or '$12.34'
    elif matches := re.search(r"^(.)((?:[0-9]+)(?:\.[0-9]{2})?)$", user_input):
        val_symbol = matches.group(1)
        val_code = get_code(val_symbol)

        try:
            val_amount = float(matches.group(2))
        except ValueError:
            sys.exit("Unable to convert to float")
        else:
            return val_amount, val_code

    # format 4: '12$' or '12.34$'
    elif matches := re.search(r"^((?:[0-9]+)(?:\.[0-9]{2})?)(.)$", user_input):
        val_symbol = matches.group(2)
        val_code = get_code(val_symbol)

        try:
            val_amount = float(matches.group(1))
        except ValueError:
            sys.exit("Unable to convert to float")
        else:
            return val_amount, val_code

    else:
        sys.exit("Input invalid.")
        

def get_code(sym: str) -> str:
    # dictionary of symbols to code
    symbols = {"$": "USD",
               "£": "GBP",
               "₴": "UAH",
               "¥": "JPY",
               "₣": "INR",
               "R": "ZAR"}
    
    try:
        return symbols[sym]
    except KeyError:
        sys.exit("Currency not accepted.")


def convert_to_euros(val: float, code: str) -> float:
    # access API
    try:
        response = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=" + API_KEY + "&symbols=" + accepted_symbols)
    except requests.RequestException:
        sys.exit("Cannot access API.")
    else:
        # if API works, then pull JSON
        try:
            o = response.json()
        except requests.JSONDecodeError:
            sys.exit("Could not read JSON.")
        else:
            return val / o["rates"][code]


if __name__ == "__main__":
    main()