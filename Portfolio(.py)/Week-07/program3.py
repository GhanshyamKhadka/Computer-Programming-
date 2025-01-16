'''Write a program that manages a list of countries and their capital cities. It should
 prompt the user to enter the name of a country. If the program already "knows"
 the name of the capital city, it should display it. Otherwise it should ask the user to
 enter it. This should carry on until the user terminates the program (how this
 happens is up to you).'''

def main():
    countries = {}

    while True:
        country = input("Enter the name of a country (or type 'exit' to quit): ").strip()
        if country.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        if country in countries:
            print(f"The capital of {country} is {countries[country]}.")
        else:
            capital = input(f"I don't know the capital of {country}. Please enter it: ").strip()
            countries[country] = capital
            print(f"Thank you! I've added {country} with its capital {capital}.")

if __name__ == "__main__":
    main()



