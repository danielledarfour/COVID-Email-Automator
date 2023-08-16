# COVID Email Automator
When vaccines were finally released during the COVID outbreak, pharmacies became very busy making appointments. This program automates that process by having the user input an excel file with names, email addresses, and first COVID appointment dates; having the user customize their email to be sent out, and automatically sending the email to each address with second COVID appointment dates.
- Leverage of Pandas for data manipulation, dateutil for date calculations, and Python’s built-in smtplib and
email.message libraries for email sending
- Intuitive user instructions guide the process of uploading an Excel file with patient data, ensuring seamless data
integration
- Extracts patient names, emails, and vaccination dates from the uploaded Excel sheet, and utilizes dateutil to
calculate the corresponding second vaccine dates
- Dynamically creates personalized email content with appointment information, empowering healthcare professionals
to communicate effectively
- Incorporates error handling to identify and handle invalid email addresses, guaranteeing the successful delivery of
notifications

<br />
*Program implemented on Replit*

https://github.com/danielledarfour/COVID-Email-Automator/assets/67208809/601f2764-261a-4898-b44f-6e1a88a2dd6f

## How to Clone and Test Program <br />
1.
```console
danidarf@DanisLaptop:~$ https://github.com/danielledarfour/COVID-Email-Automator.git
```
2. Open Folder in IDE and run
3. Use "Test.xlsx" Excel file already uploaded
4. When system prompts you to enter email address, use "local.pharmacy1234@gmail.com"
5. When system prompts you to enter email password, use "localpharm"
6. Log into provided gmail account to see results 

## How to Run Program With Personal Email <br />
**MUST USE A GMAIL ACCOUNT** 
1. Go to https://myaccount.google.com/u/0/apppasswords
<br />

![Image of linked page](https://github.com/danielledarfour/COVID-Email-Automator/assets/67208809/54be71ea-8a90-416e-ad55-0d4b858eaf77)
<br />

3. Select Mail app and the device you're using
4. Generate password and use that when system prompts you to enter email password
5. Run program as usual

## How to Run Program with Personal Excel File
1. Excel file must be formatted like this:
- Table must be on first sheet
- Start in Box A1
- Each column must have a heading and contain names in first column, emails in second, and dates in third (can use different heading names)
<br />

![Image of sample excel file](https://github.com/danielledarfour/COVID-Email-Automator/assets/67208809/69be2ccb-1316-4367-a019-84181c597d89)
<br />

2. Upload Excel file to cloned program folder
3. Run program as usual



   
