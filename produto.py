
# SISTEMA DE PRODUTOS

produtos = []

def cadastrar_produtos():
    quantidade = int(input("Quantos produtos deseja cadastrar? "))

    for i in range(quantidade):
        print(f"\nCadastro do produto {i + 1}")

        nome = input("Nome: ")
        preco = float(input("Preço: R$ ").replace(",", "."))
        categoria = input("Categoria: ")

        produto = {
            "nome": nome,
            "preco": preco,
            "categoria": categoria
        }

        produtos.append(produto)

    print("\nProdutos cadastrados com sucesso!")


def filtrar_produtos():
    limite = float(input("Informe o preço limite: R$ "))

    print("\n1 - Acima do valor")
    print("2 - Abaixo do valor")

    opcao = input("Escolha: ")

    print("\nPRODUTOS FILTRADOS")

    for produto in produtos:
        if opcao == "1" and produto["preco"] > limite:
            print(f'{produto["nome"]}: R$ {produto["preco"]:.2f}')

        elif opcao == "2" and produto["preco"] < limite:
            print(f'{produto["nome"]}: R$ {produto["preco"]:.2f}')


def ordenar_produtos():
    crescente = sorted(produtos, key=lambda p: p["preco"])

    decrescente = sorted(
        produtos,
        key=lambda p: p["preco"],
        reverse=True
    )

    print("\nORDEM CRESCENTE")

    for produto in crescente:
        print(f'{produto["nome"]}: R$ {produto["preco"]:.2f}')

    print("\nORDEM DECRESCENTE")

    for produto in decrescente:
        print(f'{produto["nome"]}: R$ {produto["preco"]:.2f}')


def categorias_unicas():
    categorias = set()

    for produto in produtos:
        categorias.add(produto["categoria"])

    print("\nCATEGORIAS ÚNICAS")

    for categoria in categorias:
        print(categoria)


def calcular_estatisticas():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return None

    precos = [produto["preco"] for produto in produtos]

    estatisticas = (
        min(precos),
        max(precos),
        sum(precos) / len(precos)
    )

    return estatisticas


def gerar_relatorio():
    estatisticas = calcular_estatisticas()

    if estatisticas is None:
        return

    menor, maior, media = estatisticas

    print("\n========== RELATÓRIO FINAL ==========")

    print(f"Total de produtos: {len(produtos)}")
    print(f"Menor preço: R$ {menor:.2f}")
    print(f"Maior preço: R$ {maior:.2f}")
    print(f"Média dos preços: R$ {media:.2f}")

    categorias = {p["categoria"] for p in produtos}

    print(f"Total de categorias: {len(categorias)}")

    print("\nPRODUTOS CADASTRADOS")

    for produto in produtos:
        print(
            f'Nome: {produto["nome"]} | '
            f'Preço: R$ {produto["preco"]:.2f} | '
            f'Categoria: {produto["categoria"]}'
        )


def main():
    while True:
        print("\n========== MENU ==========")
        print("1 - Cadastrar produtos")
        print("2 - Filtrar produtos")
        print("3 - Ordenar produtos")
        print("4 - Categorias únicas")
        print("5 - Estatísticas")
        print("6 - Relatório final")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produtos()

        elif opcao == "2":
            filtrar_produtos()

        elif opcao == "3":
            ordenar_produtos()

        elif opcao == "4":
            categorias_unicas()

        elif opcao == "5":
            resultado = calcular_estatisticas()

            if resultado:
                print(f"Menor: R$ {resultado[0]:.2f}")
                print(f"Maior: R$ {resultado[1]:.2f}")
                print(f"Média: R$ {resultado[2]:.2f}")

        elif opcao == "6":
            gerar_relatorio()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
