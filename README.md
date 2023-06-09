# Currency Exchange Rate Calculator
#### Video Demo:
#### Description: using the ExchangeRates API to convert a user-provided currency value to Euros

This program will serve as a calculator to quickly convert a currency amount to Euros by grabbing the latest exchange rates via an API. First, I had to make an account with Exchangerate API to get my own API key to make requests.

For the sake of this project and reduce bandwidth, I limited the currency types for conversion to US dollar (USD), British pound (GBP), Ukrainian hyrvnia (UAH), Japanese yen (JPY), Indian rupee (INR), and South African rand (ZAR). I retrieved a list of currency symbols ExchangeRatesAPI accepts and used that to select the six currency types. I will store these symbols and their three-character currency code in a dictionary.

I want to structure my program in a way where my user inputs a currency value in the command line with the currency symbol or three-character code, in any order, and see what the equivalent amount is in Euros. In other words, "$10", "10$", "USD 10", and "10 USD" would be acceptable input. If the user does not provide a valid currency code or number, then the program ends and the user must run it again to access the calculator.

The calculator will access the API once a day, instead of each time the program is run, to avoid going over the limit. 