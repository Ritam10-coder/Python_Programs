def check_season(month):
    month=month.lower()
    if month in ['november','december','january']:
      return 'Winter'
    elif month in ['february','march']:
      return 'Spring'
    elif month in['april','may','june','july']:
       return 'Summer'
    elif month in['azugust','september','october']:
       return 'Autumn'
month=str(input("Enter the month:"))
print(check_season(month)) 
