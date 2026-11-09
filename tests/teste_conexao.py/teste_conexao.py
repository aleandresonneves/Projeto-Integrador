import psycopg2

try:
    conexao = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="alunocceia"
    )

    print("Conexão com PostgreSQL realizada!")

    conexao.close()

except Exception as erro:
    print("Erro na conexão:", erro)