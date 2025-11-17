from datetime import date
from tkinter.font import names


class Employee:
    def __init__(self, name:str, date_of_birth:date, position:str,
                 admission:date, work_regime:int, hourly_rate:float, departament:str="0"):
        try:
            if isinstance(name,str):
                if not  (2 <= len(name) <= 50):
                    raise ValueError("Nome deve conter entre 2 e 50 caracteres!")
            else:
                raise TypeError("Nome deve ser um texto!")

            if isinstance(date_of_birth,date):
                date_limit = date.today()
                if date_of_birth > date_limit.replace(year=date_limit.year - 16):
                    raise ValueError("A idade mínima é 16 anos.")

            if isinstance(position,str):
                if not (3 <= len(position) <= 30):
                    raise ValueError("Cargo deve conter entre 3 e 30 caracteres!")

            if isinstance(admission,date):
                admission_date = date.today()
                if admission > admission_date:
                    raise ValueError("Data não pode ser futura!")

            if isinstance(work_regime,int):
                if not (10 <= work_regime <= 60):
                    raise ValueError("Quantidade horas semanais deve ser entre 10 e 60!")

            if isinstance(hourly_rate,float):
                if hourly_rate < 0.01:
                    raise ValueError("Valor da hora deve ser a partir de 0.01!")
        except Exception as error:
            raise error

        else:
            self.name = name
            self.date_of_birth = date_of_birth
            self.position = position
            self.admission = admission
            self.work_regime = work_regime
            self.hourly_rate = hourly_rate
            self.departament = departament

    def __str__(self) -> str:
        data_output = ( f"Nome: {self.name}"
                        f"Data de nascimento: {self.date_of_birth}"
                        f"Cargo: {self.position}"
                        f"Data de admissão: {self.admission}"
                        f"Regime de trabalho: {self.work_regime}"
                        f"Valor da hora trabalhada: {self.hourly_rate}"
                        f"Departamento: {self.departament}")
        return data_output

    def congratulate_employee (self) -> None:
            current_day = date.today()
            if (self.date_of_birth.day == current_day.day) and (self.date_of_birth.month == current_day.month):
                print(f"Feliz aniversário {self.name}!")

    def calculate_salary (self, month:int) -> float:
        try:
            if isinstance(month,int):
                if not 1 <= month <= 12:
                    print("Mês inválido")
        except Exception as error:
            raise error

        weeks = [4, 4.5, 4, 4, 4, 4, 4, 4, 4.5, 4.5, 4, 4.5]
        for m in range(weeks):
            i = weeks.index(m)
            if month == (i + 1):
                total_salary = weeks[i] * self.work_regime * self.hourly_rate
                if total_salary <= 5000:
                    net_salary = total_salary - (total_salary * 0.08) - (total_salary * 0.01)
                elif total_salary <= 5000:
                    net_salary = total_salary - (total_salary * 0.08) - (total_salary * 0.01)
                elif total_salary <= 7500:
                    net_salary = total_salary - (total_salary * 0.08) - (total_salary * 0.125) - (total_salary * 0.01)
                elif total_salary <= 50000:
                    net_salary = total_salary - (total_salary * 0.08) - (total_salary * 0.275) - (total_salary * 0.01)
                else:
                    net_salary = total_salary - (total_salary * 0.08) - (total_salary * 0.375) - (total_salary * 0.01)



