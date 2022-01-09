import os.path
import pandas as pd
# variables allocated to the storage path of files to be edited
search_csv = 'input/employeedata.csv'
search_xlsx = 'input/employeedata.xlsx'

# variables allocated to the storage path where new files will be stored
output_csv = 'output/new_employeedata.csv'
output_xlsx = 'output/new_employeedata.xlsx'

# gets and returns csv file


def get_csv():
    csv_file = pd.read_csv(search_csv)
    return csv_file

# gets and returns xlsx file


def get_xlsx():
    xlsx_file = pd.read_csv(search_xlsx)
    return xlsx_file


def convert_to_list():
    data = None

    if os.path.exists(search_csv):
        data = get_csv()
    else:
        data = get_xlsx()
    oldemail = data["email"].tolist()
    newemail = []
    name = data["name"].tolist()
    number = data["number"].tolist()

    for email in oldemail:
        newemail.append(email.replace("helpinghands.cm", "handsinhands.org"))

    print(".....")
    output_updated_file(name, newemail, number)



def output_updated_file(name, newemail, number):

    newData = {"Names": name, "Email": newemail, "Number": number}
    df = pd.DataFrame(newData)
    print("Enter 1 for CSV or 2 for XLSX")
    input_chioce = None
    try:
      input_chioce = int(input("1 or 2 : "))
    except ValueError:
        print("Try Again")

    if input_chioce == 1:
        df.to_csv(output_csv)

    elif input_chioce == 2:
        df.to_excel(output_xlsx)
    else:
        print("Try Again")


def output_emails():
    convert_to_list()


output_emails()






