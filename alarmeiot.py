from gpiozero import LED, Buzzer
from time import sleep, time

# Simulação de teclado (substitua por leitura real de GPIO ou interface física)
from pynput.keyboard import Listener

# Configurações dos dispositivos
led_verde = LED(11)
led_vermelho = LED(12)
buzzer = Buzzer(10)

# Estado inicial
senha_correta = "1234"
senha_digitada = ""
tentativas = 0
sistema_armado = True
alarme_ativado = False
alarme_inicio = 0
duracao_alarme = 10  # segundos

print("Sistema ARMADO. Digite a senha.")

def ativar_alarme():
    global alarme_ativado, alarme_inicio
    alarme_ativado = True
    alarme_inicio = time()
    print("ALERTA! Alarme ativado.")

def desativar_alarme():
    global alarme_ativado, tentativas, sistema_armado
    alarme_ativado = False
    tentativas = 0
    sistema_armado = True
    led_vermelho.on()
    buzzer.off()
    print("Alarme finalizado. Sistema ARMADO.")

def processar_tecla(tecla):
    global senha_digitada, tentativas, sistema_armado, alarme_ativado

    print(f"Tecla: {tecla}")

    if alarme_ativado:
        if time() - alarme_inicio >= duracao_alarme:
            desativar_alarme()
        else:
            led_vermelho.toggle()
            buzzer.toggle()
        return

    if tecla == '#':
        if senha_digitada == senha_correta:
            sistema_armado = False
            led_verde.on()
            led_vermelho.off()
            print("Senha correta! Sistema DESARMADO.")
        else:
            tentativas += 1
            print(f"Senha incorreta! Tentativa {tentativas}")
            if tentativas >= 3:
                ativar_alarme()
        senha_digitada = ""

    elif tecla == '*':
        sistema_armado = True
        senha_digitada = ""
        tentativas = 0
        led_verde.off()
        led_vermelho.on()
        print("Sistema ARMADO novamente.")

    elif tecla.isdigit():
        if len(senha_digitada) < 6:
            senha_digitada += tecla
            print(f"Senha parcial: {senha_digitada}")

# Escuta do teclado (simulação)
def on_press(key):
    try:
        tecla = key.char
        if tecla in '0123456789*#':
            processar_tecla(tecla)
    except AttributeError:
        pass

with Listener(on_press=on_press) as listener:
    listener.join()