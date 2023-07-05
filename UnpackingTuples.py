def calcular_imposto(valor):
    ir = 0.2 * valor
    csll = 0.0375 * valor
    iss = 0.85 * valor
    return ir, csll, iss

venda = 1000
impostos = calcular_imposto(venda)
print(impostos)

ir, csll, iss = calcular_imposto(venda)
print(ir,csll,iss)