# Problem Set 1B - House Hunting
# Autor: Caio Vieira Hilário
# Curso: MIT 6.0001 (Introduction to Computer Science in Python)
# Objetivo: Calcular o número de meses necessários para juntar a entrada de uma casa
# Data: Outubro/2025

annual_salary = float(input("Entre com o seu salário anual: "))

def savingsCalc(annual_salary, portion_saved):
    """Recebe o salario anual e a porcentagem do salario mensal guardada para 
    dar de entrada em uma casa, os dois são float. Retorna o dinheiro guardado 
    apos 36 meses (3 anos)"""
    semi_annual_raise = 0.07 #aumento salarial semestral
    r = 0.04 #retorno anual de investimentos
    salary = annual_salary

    semi_anual_indicator = 1 #indicador semestral
    current_savings = 0

    # Verifica mês a mês se o dinheiro guardado é menor que o valor da entrada, adicionando
    # os investimentos e a porcentagem do salário salvo para o objetivo.
    for month in range(36):
        month_salary = salary/12
        investment = current_savings * r/12
        current_savings += month_salary*portion_saved + investment

        # incrementa o indicador semestral até o sexto mês para saber quando aumentar 
        # o sálario, atualiza o salário e reseta o indicador semestral
        if semi_anual_indicator == 6:
            semi_anual_indicator = 0
            salary = salary + salary*semi_annual_raise
        semi_anual_indicator += 1

    return current_savings

low = 0
high = 10000
ans = (high + low)//2
portion_saved = ans/10000.00
num_guesses = 0
months = 0
current_savings = 0
epsilon = 100 #erro de 100 dolares do valor da entrada
total_cost = 1000000 #preço da casa sos sonhos
portion_down_payment = 0.25 #entrada (porcentagem do valor total da casa)
down_payment = portion_down_payment*total_cost #valor da entrada

while abs(current_savings - down_payment) > epsilon and num_guesses < 100:
    num_guesses += 1
    current_savings = savingsCalc(annual_salary, portion_saved)

    if current_savings < down_payment:
        if portion_saved > 1:
            print("Não é possivel pagar a entrada em três anos.")
            break
        low = ans
    else: 
        high = ans
    ans = (high + low)//2
    portion_saved = ans/10000.00

if portion_saved < 0.95:   
    print(f"A melhor porção decimal a ser guardada do seu salário mensal é: {portion_saved}")
    print(f"O número de passos do bissection search foram: {num_guesses}")

