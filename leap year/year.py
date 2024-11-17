def leap_year(year):
    """Determine whether a given year is a leap year.

    :param year: year to check
    :return bool: True or False depending on the check in the function  
    """

    division_results = []

    if year % 4 == 0:
        division_results.append(True)
    else:
        division_results.append(False)
    
    if year % 100 == 0:
        division_results.append(True)
    else:
        division_results.append(False)
    
    if year % 400 == 0:
        division_results.append(True)
    else:
        division_results.append(False)


    if division_results[0] == True and division_results[1] == True and division_results[2] == False:
        return False
    elif division_results[0] == True and division_results[1] == True and division_results[2] == True:
        return True
    elif division_results[0] == True and division_results[1] == False and division_results[2] == False:
        return True
    elif division_results[0] == False:
        return False
    elif division_results[0] == False and division_results[1] == False and division_results[2] == False:
        return False

    
print(leap_year(2015))