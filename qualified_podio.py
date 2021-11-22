def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    lista1 = [tempo_chegada1, tempo_chegada2, tempo_chegada3]
    podio_ordenado = sorted(lista1)
    podio = (
            f"1 - {podio_ordenado[0]} minutos\n"
            f"2 - {podio_ordenado[1]} minutos\n"
            f"3 - {podio_ordenado[2]} minutos\n"
        )
    return podio