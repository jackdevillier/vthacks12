#Libraries to Import
import csv


# Main
def main():
    print(ReadCsv("Alabama"))



#
# Functions
#

# Data Collection
def ReadCsv(state):
    data = []
    type = []
    amount = []
    File_Name = state + " Bias Types 2022.csv"
    with open(File_Name, mode='r') as csvfile:
        file = csv.reader(csvfile)
        for row in csvfile:
            data.append(row)
    data[0] = "Type,Amount"
    for i in range(len(data)):
        data[i] = data[i].replace('\n','')
        data[i] = data[i].split(",")
    total, data = CheckLGBTQ(data)
    return data, total



#Checking data from list for LGBTQ+ Hate Crimes
def CheckLGBTQ(data):
    total = 0
    Marked = []
    KeyWords = ["Gay", "Lesbian", "Bisexual", "Transgender", "Non-conforming"]
    for i in range(len(data)):
        for j in range(len(KeyWords)):
            if data[i][0].find(KeyWords[j]) != -1:
                total = total + int(data[i][1])
            else:
                Marked.append(i)
    for k in range(len(Marked)):
        print(Marked[k])
    return total, data


# Runs main
main()