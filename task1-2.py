def total_salary(path):
    sum = 0
    devs = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    _, salary = line.strip().split(',')
                    salary = int(salary)
                    sum += salary
                    devs += 1
                except ValueError:
                    print(f"Некоректний формат даних: {line.strip()}")
            
            if devs == 0:
                return 0, 0 

            avg_salary = sum / devs
            return sum, avg_salary
    except FileNotFoundError:
        return None
    


def get_cats_info(path):
    list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    id, name, age = line.strip().split(',')
                    list.append({'id': id, 'name': name, 'age': age})
                except ValueError:
                    print(f"Некоректний формат даних: {line.strip()}")

            return list

    except FileNotFoundError:
        return None