from application.people import get_employees
from application.salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    current_date = datetime.now().date()
    print(f'Текущая дата {current_date}')
    get_employees()
    calculate_salary()