import microbit

# Define la variable para el sensor FC-51
sensorFC51 = microbit.pin1

# Define una variable para almacenar el estado del sensor
estadoSensor = False

# Inicializa el sensor
sensorFC51.set_pull(microbit.Pull.UP)

# Bucle principal
while True:
  # Lee el estado del sensor
  estadoSensor = sensorFC51.read_digital()

  # Si el sensor está activado, muestra un corazón
  if estadoSensor:
    microbit.display.show(microbit.Image.HEART)
    microbit.sleep(500)
  else:
    # Si el sensor no está activado, muestra una cruz
    microbit.display.show(microbit.Image.CROSS)
    microbit.sleep(500)

