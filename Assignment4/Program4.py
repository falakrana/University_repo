# Average Salary Excluding the Minimum and Maximum Salary


def average_salary(salary):
    salary.sort()
    salary.pop(0)
    salary.pop(-1)
    average = sum(salary) / len(salary)
    return f"{average:.{5}f}"


salary = [4000, 2000, 3000, 1000]
print(average_salary(salary))



