# 1 - ENTRADA/COLETA DE DADOS
date = input("Qual é a data (DD/MM/AAAA)? "); # Data de referência no formato Dia-Mês-Ano

# O replace é utilizado para substituir a vírgula por ponto, caso o usuário digite a vírgula ao invés do ponto.
litrosDeAgua = float(
    input("Quantos litros de água você consumiu hoje? (Aprox. em litros) ").replace(",", ".")
); # Quantidade de água consumida em litros

kwhDeEnergia = float(
    input("Quantos kWh de energia você consumiu hoje? ").replace(",", ".")
); # Quantidade de energia consumida em kWh

kgDeResiduosNaoReciclavies = float(
    input("Quantos kg de resíduos não recicláveis você gerou hoje? ").replace(",", ".")
); # Quantidade de resíduos não reciclados em kg

percentualDeResiduosReciclados = float(
    input("Qual o percentual de resíduos reciclados no total? (em %) ").replace(",", ".")
); # Percentual de resíduos reciclados

meioDeTransporte = int(
    input("Qual o meio de transporte que você usou hoje?\n1. Transporte público (ônibus, metrô, trem).\n2. Bicicleta\n3. Caminhada\n4. Carro (combustível fósseis)\n5. Carro elétrico\n6. Carona compartilhada\n")
); # Meio de transporte utilizado