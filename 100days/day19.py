print("")

loan = int(input("Enter the loan Amount : "))
apr = 0.05

for i in range (10):
    loan+=(loan*apr)
    print("Year", i+1, "is", round(loan,2))
