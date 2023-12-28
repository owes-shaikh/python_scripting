## Age Calculator using Python
Age Calculator is an amazing application to create as a beginner in any programming language. To create an age calculator, you need two dates:
today’s date
date of birth
You can either ask the user for both dates or just ask for the date of birth and use today’s date from the computer itself. 
Asking for the birthday only seems like a more user-friendly option. So here’s how to create an age calculator using Python:


In the above code:

we have to first defined a Python function where I am asking for three user inputs:
    
    - y: year of birth 
    - m: month of birth 
    - d: date of birth
    
Then we are importing the datetime module in Python inside the function
Then in the next line, we are taking today’s date by using the datetime.now() method of the datetime module
Then we have introduced a new variable in the next line as dob, where we are using the date of birth as the input given by the user
Then we are subtracting the dob with today’s date and then dividing it by 365.25 which is returning the age of the user.
