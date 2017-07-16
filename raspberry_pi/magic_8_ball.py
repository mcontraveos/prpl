"""
Magic 8-Ball
    for use with Python, version 3 and later

This program interfaces with a Sense Hat to display the answer to a
question after being shaken like a magic 8-ball!
"""
from random import choice
from sense_hat import Sense Hat


colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'aqua': (0, 255, 255),
    'purple': (255, 0, 255),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'grey': (128, 128, 128)
}

prompt = 'Ask a question and shake me up!'

answers = [
    'But of course!',
    'Heavens, no!',
    'Definitely!',
    "Don't know, don't care.",
    "I don't know about that, but I do know it's %s degrees in here now."
]

scroll_speed = 0.03

sense = SenseHat()

sense.show_message(prompt,
                   scroll_speed=scroll_speed)

while True:
    x, y, z = sense.get_accelerometer_raw().values()
    x = abs(x)
    y = abs(y)
    z = abs(z)

    x_threshold = 2
    y_threshold = 2
    z_threshold = 2

    if x > x_threshold and y > y_threshold and z > z_threshold:
        answer = choice(answers)

        if 'degrees' in answer:
            celsius = int(sense.get_temperature_from_humidity())
            fahrenheit = (celsius * 9/5) + 32
            answer = answer % fahrenheit
        else:
            pass

        sense.show_message(answer,
                           scroll_speed=scroll_speed,
                           text_colour=colors['white'],
                           back_colour=colors['black'])
    else:
        sense.clear()