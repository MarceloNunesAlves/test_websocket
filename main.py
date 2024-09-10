from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)  # Habilita o CORS em todas as rotas do Flask

# Cria a instância do SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")  # Habilita CORS no WebSocket

# Função que será chamada a cada 10 segundos
def periodic_task():
    while True:
        # Chame o método que você deseja a cada 10 segundos
        print("Método chamado periodicamente")

        # Emitir evento para os clientes conectados, se necessário
        send_value()

        # Espera 10 segundos antes de executar novamente
        time.sleep(2)

# Envia evento
def send_value():
    socketio.emit('cotacao', round(random.randint(1, 100) + random.random(), 2))

if __name__ == '__main__':
    # Inicia a tarefa em background
    socketio.start_background_task(periodic_task)

    # Executa o servidor com suporte ao WebSocket
    socketio.run(app, allow_unsafe_werkzeug=True)