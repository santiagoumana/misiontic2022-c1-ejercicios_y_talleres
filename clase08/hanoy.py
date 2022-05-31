def hanoi(discos, torre_a = "A", torre_b = "B", torre_c = "C"):
    if discos == 1:
        print(f"Mover disco {discos} de la torre {torre_a} a la torre {torre_c}")
    else:
        hanoi(discos - 1, torre_a, torre_c, torre_b)
        print(f"Mover disco {discos} de la torre {torre_a} a la torre {torre_c}")
        hanoi(discos - 1, torre_b, torre_a, torre_c)

    
hanoi(10)
