#Libraries to Import
import csv


# Global
States = ["Alabama", "Alaska", "Arizona","Arkansas","California","Colorado",
          "Connecticut", "Delaware","District of Columbia", "Florida", "Georgia",
          "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
          "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
          "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
          "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
          "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
          "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin",
          "Wyoming"]



# Main
def main():
    print("")
    for i in range(len(States)):
        print(States[i], ReadCsv(States[i]))
        print("")
        print("---------------------------------------------")
        print("")

#
# Functions
#

# Data Collection
def ReadCsv(state):
    data = []
    type = []
    amount = []
    File_Name = state + " Bias Types 2022.csv"
    File_Name = "Data Folder\\United States of Hatecrimes\\" + File_Name
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
                Marked.append([data[i][0],data[i][1]])
            else:
                pass
    return total, Marked    


# Runs main
main()