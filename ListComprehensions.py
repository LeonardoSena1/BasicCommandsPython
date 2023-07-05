precos_produtos = {"iphone": 5000, "ipad": 9000, "airpod": 2000, "macbook": 1500}
imposto = []
for produto in precos_produtos:
    imposto.append(precos_produtos[produto] * 0.1)

print(imposto)
