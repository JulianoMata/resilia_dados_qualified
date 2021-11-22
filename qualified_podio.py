def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    lista1 = [tempo_chegada1, tempo_chegada2, tempo_chegada3]
    ordenado = sorted(lista1)
    podio = (
            f"1 - {ordenado[0]} minutos\n"
            f"2 - {ordenado[1]} minutos\n"
            f"3 - {ordenado[2]} minutos\n"
        )
    return podio