#----- MANIPULATING DATA FROM EXCEL fILE -----

import pandas as pd 

import dateutil 

import sys

class colors:
    yellow = '\033[93m' 
    red = '\033[91m' 
    bold = '\033[1m'
    reset = '\033[0m'

print(colors.yellow + colors.bold + "Instructions: Please upload your Excel file to this folder. \nMake sure you only want the first sheet of the file read and that there are 3 columns labeled and filled with information concerning the following in order: \npatient's name, email, and date of their first covid vaccine appointment."+ colors.reset) 

#error handling if user does not type Excel file name correctly
while True:
  file_name = input("\nWhat is the name of your excel file? ")
  try:
    print("")
    file_readname = file_name + ".xlsx"
    print(pd.read_excel(file_readname)) 
  except:
    print("You may have spelled the file name wrong. Also, you do not have to include the '.xlsx'")
  else: 
    break

df = pd.read_excel(file_readname)

#stores the heading of each column into a variable
name_head = list(df.columns)[0]
email_head = list(df.columns)[1]
date_head = list(df.columns)[2]

#creates a list of names, emails, and dates from excel file
names = df[name_head].tolist()
emails = df[email_head].tolist()
dates = df[date_head].tolist()

#increments each date by 1 month
for i in range(len(dates)):
  dates[i] = dates[i] + dateutil.relativedelta.relativedelta(months=1)

#new date heading to be used in new dataframe
date_head = "2nd Vaccine Date:"

#new dataframe created with new dates
new_data = {name_head: names, email_head: emails, date_head: dates}

new_df = pd.DataFrame(new_data)

date_head2 = list(new_df.columns)[2]
email_head2 = list(new_df.columns)[1]
dates2 = new_df[date_head2].tolist()
emails2 = new_df[email_head2].tolist()

print("")
print(new_df)

#----- AUTOMATING EMAIL SENDING -----

import smtplib

from email.message import EmailMessage 

date_head2 = list(new_df.columns)[2]
dates2 = new_df[date_head2].tolist()

answer = "n"

#confirm function to be called to verify user's inputs
def confirm(email_part):
  while True:
    
    confirmation = input("\nAre you sure:" + "\n" + colors.bold + email_part + colors.reset + "\nYes/No. ").lower()
    global answer
    answer = confirmation[0]
    if answer == "y":
      return (colors.green + "Confirmed." + colors.reset)
    elif answer == "n":
      break 
    else:
      print(colors.red + "Invalid input. Please try again." + colors.reset)
      continue
  return

#series of questions to log into user's email and configure the content of the email to be sent out
while answer != "y":
  email_address = input("\nWhat is your email address for Gmail?\n")
  print(confirm(email_address))
  
answer = "n"

while answer != "y":
  email_password = input("\nWhat is your email password for Gmail?\n")
  print(confirm(email_password))

answer = "n"

while answer != "y":
  subject = input("\nWhat would you like the subject of the email to be?\n")
  print(confirm(subject))

answer = "n"

while answer != "y":
  message = input("\nWhat would you like the message of the email to be? The program will include this after your message:\n\nYour appoinment date:" + "\n*appoinment date*" + "\n\nType here:\n")
  print(confirm(message))

print(colors.bold + "\nPlease Wait" + colors.reset)

#configures emails and sends them to the correct addresses
#if email in dataframe is incorrect, it's added to a list of invalid emails
invalid_emails = []
for i in range(len(new_df[date_head2])):

  msg = EmailMessage()
  msg["Subject"] = subject
  msg["From"] = email_address
  msg["To"] = emails2[i]
  msg.set_content("{} \n\nYour appointment date:\n{} {}, {}".format(message, dates2[i].strftime('%B'), dates2[i].day, dates2[i].year))
  try: 
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
      smtp.login(email_address, email_password)
      smtp.send_message(msg)

  except:
    invalid_emails.append(emails[i])
    continue         

#either tells user that emails were sent or that some emails were not able to send due to incorrect email typed in excel file
if len(invalid_emails) == 0:
  print(colors.green + "\nEmails sent successfully")
else:
  print(colors.red + ("\nEmails to these email addresses did not send: ") + (str(", ".join(map(str, invalid_emails)))) + colors.reset)

