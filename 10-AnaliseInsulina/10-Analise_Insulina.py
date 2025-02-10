import re  # Importa o módulo de expressões regulares para manipular texto

# 1. Abrindo e lendo o arquivo com a sequência original da pré-pró-insulina
with open('./10_preproinsulin-seq.txt', 'r') as arquivo:
    sequencia = arquivo.read()  # Lê o conteúdo do arquivo e armazena na variável 'sequencia'

# 2. Usando expressão regular para limpar a sequência
# - Remove a palavra 'ORIGIN'
# - Remove todos os números presentes
# - Remove os caracteres '//' no final
# - Remove espaços e quebras de linha
sequencia_limpa = re.sub(r'ORIGIN|\d+|//|\s|\n', '', sequencia)

# 3. Exibir a sequência limpa no terminal para conferência
print(f'Sequência limpa (110 caracteres esperados): {sequencia_limpa}')

# 4. Salvando a sequência limpa em um novo arquivo
with open('10a_preproinsulin-seq-clean.txt', 'w') as arquivo_limpo:
    arquivo_limpo.write(sequencia_limpa)  # Escreve a sequência limpa no arquivo

# 5. Extraindo partes específicas da sequência e salvando em arquivos

# - A sequência sinal corresponde aos aminoácidos de 1 a 24 (índices 0 a 23 no Python)
sequencia_sinal = sequencia_limpa[0:24]
with open('10b_lsinsulin-seq-clean.txt', 'w') as arquivo:
    arquivo.write(sequencia_sinal)

# - A cadeia B da insulina corresponde aos aminoácidos de 25 a 54 (índices 24 a 54)
b_sequencia_cadeia = sequencia_limpa[24:54]
with open('10c_binsulin-seq-clean.txt', 'w') as arquivo:
    arquivo.write(b_sequencia_cadeia)

# - A cadeia C da insulina corresponde aos aminoácidos de 55 a 89 (índices 54 a 89)
c_sequencia_cadeia = sequencia_limpa[54:89]
with open('10d_cinsulin-seq-clean.txt', 'w') as arquivo:
    arquivo.write(c_sequencia_cadeia)

# - A cadeia A da insulina corresponde aos aminoácidos de 90 a 110 (índices 89 a 110)
a_sequencia_cadeia = sequencia_limpa[89:110]
with open('10e_ainsulin-seq-clean.txt', 'w') as arquivo:
    arquivo.write(a_sequencia_cadeia)

# 6. Exibir os resultados finais no terminal para conferência
print(f'Sequência Sinal (24 caracteres): {sequencia_sinal}')
print(f'Sequência Cadeia B (30 caracteres): {b_sequencia_cadeia}')
print(f'Sequência Cadeia C (35 caracteres): {c_sequencia_cadeia}')
print(f'Sequência Cadeia A (21 caracteres): {a_sequencia_cadeia}')

# ---- Explicação das variáveis e comandos ----
# - 'sequencia': Armazena o conteúdo lido do arquivo original.
# - 'sequencia_limpa': Contém a sequência filtrada sem palavras desnecessárias, números e símbolos.
# - 'sequencia_sinal', 'b_sequencia_cadeia', 'c_sequencia_cadeia', 'a_sequencia_cadeia':
#   Guardam partes específicas da sequência para posterior salvamento.
#
# Comandos usados:
# - .read(): Lê todo o conteúdo de um arquivo e retorna como uma string.
# - .sub(): Substitui padrões na string baseando-se em uma expressão regular.
# - .write(): Escreve uma string em um arquivo, sobrescrevendo qualquer conteúdo anterior.