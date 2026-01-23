def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                isYearLeap = True
            else:
                isYearLeap = False
        else:
            isYearLeap = True
    else:
        isYearLeap = False
    
    return isYearLeap

def days_in_month(year_input, month_input):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    isYearInputLeap = is_leap(year_input)
    if isYearInputLeap:
        month_days[1] = 29
    days_output = month_days[month_input - 1]
    return days_output

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
