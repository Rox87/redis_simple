import redis

# ON WSL
#curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
#echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
#sudo apt-get update
#sudo apt-get install redis
#sudo service redis-server start

# OR DOCKER
# docker run --name my-redis -p 6379:6379 -d redis

# Conectando ao Redis (substitua por suas configurações, se necessário)
r = redis.Redis(host='127.0.0.1', port=6379,password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81', db=0)

# Testando a conexão
try:
    r.ping()
    print("Conectado ao Redis!")
except redis.ConnectionError:
    print("Falha ao conectar ao Redis")
    exit()  # Encerrar o script se não conseguir conectar

# Adicionar uma chave e valor no Redis
r.set('nome', 'João')

# Recuperar o valor da chave 'nome'
nome = r.get('nome')
# Verifica se 'nome' não é None antes de decodificar
if nome is not None:
    print(f"Nome armazenado no Redis: {nome.decode('utf-8')}")
else:
    print("Chave 'nome' não encontrada no Redis.")

# Inicializando e incrementando um contador
r.set('contador', 0)
r.incr('contador')  # Incrementa o valor

# Recuperando o valor do contador
contador = r.get('contador')
# Verifica se 'contador' não é None antes de decodificar
if contador is not None:
    print(f"Contador: {contador.decode('utf-8')}")
else:
    print("Chave 'contador' não encontrada no Redis.")