# Problem Set 1B - House Hunting
# Autor: Caio Vieira Hilário
# Curso: MIT 6.0001 (Introduction to Computer Science in Python)
# Objetivo: Calcular o número de meses necessários para juntar a entrada de uma casa
# Data: Outubro/2025

total_cost = float(input("Entre com o valor da casa que quer comprar: "))
annual_salary = float(input("Entre com o seu salário anual: "))
portion_saved = float(input("Entre com a porcentagem do seu salário (em forma decimal) " \
" mensal que vai guardar: ")) #porcentagem do salário para economia da casa
semi_annual_raise = float(input("Qual a porcetagem do seu aumento salarial " \
"semestral em forma decimal? "))

portion_down_payment = 0.25 #entrada (porcentagem do valor total da casa)
r = 0.04 #retorno anual de investimentos

current_savings = 0
month = 0
down_payment = portion_down_payment*total_cost #valor da entrada
semi_anual_indicator = 1 #indicador semestral

# Verifica mês a mês se o dinheiro guardado é menor que o valor da entrada, adicionando
# os investimentos e a porcentagem do salário salvo para o objetivo.
while current_savings < down_payment:
    month_salary = annual_salary/12
    investment = current_savings * r/12
    current_savings += month_salary*portion_saved + investment
    month += 1

    # incrementa o indicador semestral até o sexto mês para saber quando aumentar 
    # o sálario, atualiza o salário e reseta o indicador semestral
    if semi_anual_indicator == 6:
        semi_anual_indicator = 0
        annual_salary = annual_salary + annual_salary*semi_annual_raise
    semi_anual_indicator += 1

print(f"Número de meses: {month}")