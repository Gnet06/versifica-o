while True:
    # 1 - ENTRADA/COLETA DE DADOS
    date = input("Qual é a data (DD/MM/AAAA)? "); # Data de referência no formato Dia-Mês-Ano

    try:
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
    except ValueError:
        print("Erro: Valor inválido. Por favor, insira um número válido.");
        continue; # O continue é utilizado para reiniciar o loop caso ocorra um erro de entrada de dados.
    except KeyboardInterrupt:
        print("\nPrograma encerrado.");
        break;
    # O try e except são utilizados para tratar erros de entrada de dados, como valores inválidos ou tipos de dados incorretos.


    # 2 - CLASSIFICAÇÃO DE SUSTENTABILIDADE
    nivelDeConsumoDeAgua = "";
    nivelDeConsumoDeEnergia = "";
    nivelDeGeracaoDeResiduosNaoReciclaveis = "";
    nivelDeUsoDeTransporte = "";

    # Menor que 150 litros de água é considerado alto, entre 150 e 200 litros é moderado e acima de 200 litros é considerado baixo.
    if litrosDeAgua < 150:
        nivelDeConsumoDeAgua = "Alta Sustentabilidade";
    elif litrosDeAgua <= 200:
        nivelDeConsumoDeAgua = "Moderada Sustentabilidade";
    else:
        nivelDeConsumoDeAgua = "Baixa Sustentabilidade";

    # O mesmo vale para o consumo de energia, onde menor que 5 kWh é considerado alto, entre 5 e 10 kWh é moderado e acima de 10 kWh é baixo.
    if kwhDeEnergia < 5:
        nivelDeConsumoDeEnergia = "Alta Sustentabilidade";
    elif kwhDeEnergia <= 10:
        nivelDeConsumoDeEnergia = "Moderada Sustentabilidade";
    else:
        nivelDeConsumoDeEnergia = "Baixa Sustentabilidade";
    
    # A geração de resíduos não recicláveis é considerada alta quando o percentual de resíduos reciclados é maior que 50%, moderada quando está entre 20% e 50% e baixa quando é menor que 20%.
    if percentualDeResiduosReciclados > 50:
        nivelDeGeracaoDeResiduosNaoReciclaveis = "Alta Sustentabilidade";
    elif percentualDeResiduosReciclados >= 20:
        nivelDeGeracaoDeResiduosNaoReciclaveis = "Moderada Sustentabilidade";
    else:
        nivelDeGeracaoDeResiduosNaoReciclaveis = "Baixa Sustentabilidade";

    # O meio de transporte é considerado sustentável quando é um transporte público, bicicleta ou caminhada, moderado quando é um carro elétrico ou carona compartilhada e baixo quando é um carro a combustão.
    if meioDeTransporte in [1, 2, 3, 5]:
        nivelDeUsoDeTransporte = "Alta Sustentabilidade";
    elif meioDeTransporte == 4:
        nivelDeUsoDeTransporte = "Baixa Sustentabilidade";
    else:
        nivelDeUsoDeTransporte = "Moderada Sustentabilidade";


    # 3 - SAÍDA DE DADOS
    print("\nSUSTENTABILIDADE");
    print(f'Consumo de água: {nivelDeConsumoDeAgua}');
    print(f'Consumo de energia: {nivelDeConsumoDeEnergia}');
    print(f'Geração de Resídusos Não Recicláveis: {nivelDeGeracaoDeResiduosNaoReciclaveis}');
    print(f'Uso de Transporte: {nivelDeUsoDeTransporte}');

    resposta = input("\nDeseja continuar? (S/N) ").strip().upper(); # O strip é utilizado para remover espaços em branco no início e no final da string, e o upper é utilizado para transformar a string em maiúscula.
    # O strip e upper são utilizados para padronizar a entrada do usuário, evitando erros de digitação.
    if resposta == "N":
        break;
    else:
        print("\n")
        continue;
# O continue é utilizado para reiniciar o loop caso o usuário deseje continuar.