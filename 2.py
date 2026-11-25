
print("PROGRESSIVE ELECTRICITY BILLING SYSTEM")

months = int(input("Enter number of months: "))

units_list = []
bill_list = []

for i in range(months):

    print("\nMonth", i + 1)

    units = int(input("Enter electricity units: "))

    if units < 0:
        print("Invalid units!")
        continue

    if units <= 100:
        bill = units * 2

    elif units <= 200:
        bill = (100 * 2) + ((units - 100) * 3)

    else:
        bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    bill = bill + 50

    if units > 300:
        bill = bill + (bill * 10 / 100)

    elif units <= 100:
        bill = bill - (bill * 5 / 100)

    units_list.append(units)
    bill_list.append(round(bill, 2))

    print("Electricity Units:", units)
    print("Monthly Bill: Rs.", round(bill, 2))


print("\n--- MONTHLY BILL COMPARISON ---")

for i in range(len(bill_list)):

    print("Month", i + 1,
          "| Units:", units_list[i],
          "| Bill: Rs.", bill_list[i])

print("\n--- UNUSUAL BILL INCREASES ---")

found = False

for i in range(1, len(bill_list)):

    if bill_list[i - 1] > 0:

        increase = bill_list[i] - bill_list[i - 1]

        percentage = (increase / bill_list[i - 1]) * 100

        if percentage > 20:
            print("Month", i + 1,
                  "Bill increased by",
                  round(percentage, 2), "%")
            found = True

if found == False:
    print("No unusual increase detected")

print("\nTotal Electricity Bill: Rs.",
      round(sum(bill_list), 2))

print("Electricity Billing Completed!")
