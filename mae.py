from nicegui import ui

# Funciones
def sumar():
    n1 = float(num1.value)
    n2 = float(num2.value)
    res = n1 + n2
    resultado.set_text(f'Resultado: {res}')

def restar():
    n1 = float(num1.value)
    n2 = float(num2.value)
    res = n1 - n2
    resultado.set_text(f'Resultado: {res}')

def multiplicar():
    n1 = float(num1.value)
    n2 = float(num2.value)
    res = n1 * n2
    resultado.set_text(f'Resultado: {res}')

def dividir():
    n1 = float(num1.value)
    n2 = float(num2.value)
    res = n1 / n2
    resultado.set_text(f'Resultado: {res}')

# Estructura de la interfaz de usuario
with ui.card().classes('w-60 m-auto p-4'):
    ui.label('Calculadora').classes('font-sans w-full text-2x1')
    num1 = ui.input('Número 1').classes('w-full')
    num2 = ui.input('Número 2').classes('w-full')
    bt_sumar = ui.button('Sumar').classes('w-full bg-blue-500 text-white').on('click', sumar)
    bt_restar = ui.button('Restar').classes('w-full bg-blue-500 text-white').on('click', restar)
    bt_multiplicar = ui.button('Multiplicar').classes('w-full bg-blue-500 text-white').on('click', multiplicar)
    bt_dividir = ui.button('Dividir').classes('w-full bg-blue-500 text-white').on('click', dividir)
    resultado = ui.label('Resultado: ').classes('w-full text-center mt-4')
   
ui.run()