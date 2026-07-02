matéria_cadastrada = []

while True:
    print("=" * 40)
    print("📚     StudyPlanner")
    print("=" * 40)

    print("1 - Adicionar Matéria")
    print("2 - Ver Matérias")
    print("3 - Registrar Horas")
    print("4 - Concluir Aula")
    print("5 - Ver Progresso")
    print("0 - Sair")
    print("=" * 40)

    opção = input("Escolha uma opção: ")
    print(f"\nvocê escolheu a opção {opção}.")

    if opção == "1":
        matéria = input("Digite o nome da matéria: ")
        aulas = input("Quantas aulas essa matéria possui? ")

        print()
        print("✅ Matéria cadastrada com sucesso!")
        print(f"Matéria: {matéria}")
        print(f"Total de aulas: {aulas}")

    elif opção == "2":
        if not matéria_cadastrada:
            print("\nNenhuma matéria cadastrada ainda.")
        else:
            print("\n--- Matérias Cadastradas ---")
            for m in matéria_cadastrada:
                print(f". {m['nome']}({m['total_aulas']} aulas)")
                print()

    elif opção == "3":
        nome_busca = input("Qual matéria? ")
        encontrou = False

        for m in matéria_cadastrada:
            if m["nome"].lower() == nome_busca.lower():
                horas = int(input("Quantas horas estudou? "))
                m["horas_estudadas"] += horas

                print(f"✅ {horas} horas registradas para {m['nome']}")
                encontrou = True
                break

        if not encontrou:
            print("❌ Matéria não encontrada.")

    elif opção == "4":
        nome_busca = input("Qual matéria? ")
        encontrou = False

        for m in matéria_cadastrada:
            if m["nome"].lower() == nome_busca.lower():
                if m["aulas_concluidas"] < m["total_aulas"]:
                    m["aulas_concluidas"] += 1
                    print(f"✅ Aula concluída! ({m['aulas_concluidas']}/{m['total_aulas']})")
                else:
                    print("✅ Todas as aulas dessa matéria já foram concluídas.")
                
                encontrou = True
                break

        if not encontrou:
            print("❌ Matéria não encontrada.")

    elif opção == "5":
        if not matéria_cadastrada:
            print("Nenhuma matéria cadastrada.")
        else:
            print("\n===== PROGRESSO =====")
            for m in matéria_cadastrada:
                # Linha corrigida e alinhada:
                porcentagem = (m["aulas_concluidas"] / m["total_aulas"]) * 100

                print(f"""
                📚 Matéria: {m['nome']}
                📖 Aulas: {m['aulas_concluidas']}/{m['total_aulas']}
                ⏱️ Horas estudadas: {m['horas_estudadas']}
                📈 Progresso: {porcentagem:.1f}%
                """)

    elif opção == "0":
        print("\nSaindo do StudyPlanner. Até mais!")
        break
        
    else:
        print("\n❌ Opção inválida.")
