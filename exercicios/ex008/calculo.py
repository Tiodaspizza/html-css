# Função para formatar números com sufixos de escala
def formatar_numero_com_escala(numero):
    # Definindo os sufixos de escala
    sufixos = ['', 'mil', 'milhões', 'bilhões', 'trilhões']

    # Encontrando a escala do número
    escala = 0
    while abs(numero) >= 1000:
        numero /= 1000.0
        escala += 1

    # Formatando o número com sufixo de escala
    return '{:.2f} {}'.format(numero, sufixos[escala])

# Dados fornecidos
custo_diagrama = 600000000  # isk
quant_item_x = 30
valor_item_x =  2000000  # isk
quant_item_y = 40
valor_item_y = 150000  # isk
custo_producao = 1000000  # isk
preco_venda = 1600000000  # isk
taxa_mediador = 0.074
imposto_mercado = 0.15

# Calculando a receita total
receita_item_x = quant_item_x * valor_item_x
receita_item_y = quant_item_y * valor_item_y
receita_total = receita_item_x + receita_item_y

# Calculando o custo total
custo_total = (
    custo_diagrama +
    custo_producao +
    (receita_total * taxa_mediador) +
    (receita_total * imposto_mercado)
)

# Calculando o lucro
lucro = preco_venda - custo_total

# Formatando o lucro com sufixo de escala
lucro_formatado = formatar_numero_com_escala(lucro)

print("Lucro: {} ISK".format(lucro_formatado))
