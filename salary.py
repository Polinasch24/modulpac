from database.people import get_employees
employees =get_employees()

rate = input("Ставка:  ")
hours = input("Количество часов:  ")

def calculate_salary ( rate, hours) :
  if hours <= 40:
    return rate*hours
  else:
    return (f"employees:(hours-40)*1.5*rate + (40*rate)")
