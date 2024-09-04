month_to_season = {
    1: 'Winter',  2: 'Winter',  3: 'Spring',
    4: 'Spring',  5: 'Spring',  6: 'Summer',
    7: 'Summer',  8: 'Summer',  9: 'Autumn',
    10: 'Autumn', 411: 'Autumn',  12: 'Winter'
}
month_number = int(input("Enter the month number : "))
season = month_to_season.get(month_number, "Invalid month number")
print(f"The season is : {season}")
