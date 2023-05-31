import requests
import config
import json
import sys
import argparse

API_KEY = config.api_key

def main():
    # starter function to see what symbols are accepted, not to be run in calculator
    hide = True
    if not hide:
        get_accepted_currencies()




    # get command-line arguments and make sure they're formatted properly
    parser = argparse.ArgumentParser(prog="Currency Exchange Rate Calculator", description="Convert your currency to Euros")
    parser.add_argument("-n", default=0, help="currency amount", type=float)
    parser.add_argument("-typ", default="EUR", help="currency code", type=str, choices=["USD", "GBP", "UAH", "JPY", "INR", "ZAR"])
    args = parser.parse_args()

    print(args)


    # convert user input


    # print out Euro value

    


def get_accepted_currencies():
    # setup API
    try:
        response = requests.get("http://api.exchangeratesapi.io/v1/symbols?access_key=" + API_KEY)
    except requests.RequestException:
        sys.exit("Cannot access API")
    else:
        # if API works, then pull JSON
        try:
            o = response.json()
        except requests.JSONDecodeError:
            sys.exit("Could not read JSON")
        else:
            print(json.dumps(o, indent=2))


def parse_input():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()