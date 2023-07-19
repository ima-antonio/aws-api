def calcular_porcentagem_similaridade(hash1, hash2):
    # Converter as strings hexadecimais para inteiros de 64 bits
    hash1_int = int(hash1, 16)
    hash2_int = int(hash2, 16)

    # Calcular a diferença entre as duas hashes usando operação XOR
    diff = hash1_int ^ hash2_int

    # Contar o número de bits diferentes (ou seja, bits iguais = 0)
    num_bits_iguais = 64 - bin(diff).count("1")

    # Calcular a porcentagem de similaridade
    porcentagem_similaridade = (num_bits_iguais / 64) * 100

    return porcentagem_similaridade

# Exemplo de uso:
hash1 = "ffffe1c080000080"
hash2 = "f0f77f8181c1c1c1"

porcentagem = calcular_porcentagem_similaridade(hash1, hash2)
print(f"Porcentagem de similaridade: {porcentagem:.2f}%")