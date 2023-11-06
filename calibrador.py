# Calibrador de taxa de frames
# Autor: Carlo Ralph De Musis

# Importando as classes necessárias das bibliotecas de hardware e tempo
from machine import Pin, Timer
import utime

# Configuração dos LEDs
led_17 = Pin(17, Pin.OUT)  # Cria um objeto Pin para controlar um LED no pino 17
led_17.value(0)            # Desliga o LED (0 representa o estado desligado)

led_14 = Pin(14, Pin.OUT)  # Cria um objeto Pin para controlar um LED no pino 14
led_14.value(1)            # Liga o LED (1 representa o estado ligado)

# Configuração do Timer
timer = Timer()

# Lista para armazenar os tempos de alternância dos LEDs
tempos = ['-' ]  # Inicializa com um traço como placeholder para o cabeçalho

# Definição da função callback que será chamada pelo timer
def alterna_led(timer):
    led_14.toggle()  # Alterna o estado do LED no pino 14
    led_17.toggle()  # Alterna o estado do LED no pino 17
    
    corrente_tempo = utime.ticks_ms()  # Obtém o tempo atual em milissegundos
    tempos.append(corrente_tempo)      # Adiciona o tempo atual à lista
    print('LED alternado ', corrente_tempo)
    # Precisão: 20 microsegundos/s (2e-5s)

# Definição da função para escrever os tempos de alternância dos LEDs em um arquivo CSV
def escreve_csv(filename, data):
    try:
        # Checa se o arquivo já existe para evitar reescrever o cabeçalho
        cabecalho = not filename in os.listdir()
        
        with open(filename, 'a') as f:  # Abre o arquivo para adicionar dados
            if cabecalho:
                f.write('Tempo (ms)\n')  # Escreve o cabeçalho se necessário
            
            for m_tempo in data:
                f.write('{}\n'.format(m_tempo))  # Escreve cada tempo registrado
            
            f.flush()  # Garante que todos os dados sejam escritos no arquivo

        # Após fechar o arquivo, verifica se o arquivo contém dados
        if filename in os.listdir():
            with open(filename, 'r') as f:
                if f.read():
                    print('Arquivo gravado com sucesso.')
                    return True
        return False
    except Exception as e:
        print('Falha ao gravar arquivo:', e)
        led_14.value(0)  # Desliga o LED do pino 14 em caso de falha
        led_17.value(0)  # Desliga o LED do pino 17 em caso de falha
        return False

# Loop principal do script
while True:            
    timer.init(period=10000, mode=Timer.PERIODIC, callback=alterna_led)  # Inicia o timer com um período de 10 segundos
    utime.sleep(300)  # Aguarda 300 segundos (5 minutos)

    timer.deinit()  # Desativa o timer
    escreve_csv('tempos.csv', tempos)  # Escreve os tempos no arquivo CSV
    
    # Alternância manual dos LEDs por 5 vezes
    for i in range(5):
        led_14.toggle()  # Alterna o estado do LED no pino 14
        led_17.toggle()  # Alterna o estado do LED no pino 17
        utime.sleep(1)   # Espera um segundo antes da próxima alternância
