"""
Magic 8-Ball
    for use with Python, version 3 and later

This program interfaces with a Sense Hat to display the answer to a
question after being shaken like a magic 8-ball!
"""

# Each line that begins with a pound-sign (#) is a comment and will not be 
# interpreted Python as an instruction. We can use this to leave helpful 
# explanations for the next person to read this program!


from random import choice
from sense_hat import Sense Hat
# A carpenter uses tools like saws and hammers to build a dresser, and he
# likely didn't make these tools himself. Likewise, we don't always make the
# tools we use in computer programming, and here, Python has supplied us with
# toolsets called "random" and "time". This is because generating random data
# and working with time are very common operations in programming, so those
# tools have been included with the Python language to aid in creating useful
# software. In software, these toolsets are often called "libraries".
#
# From the "random" library, we want to use "choice", which will pick a 
# single item at random from a set of items.
#
# The Sense Hat company has provided a Python library for interfacing with
# the Sense Hat board itself, and appropriately, they have called their library
# "sense_hat".


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
# The Sense Hat has a 64-dot display that can show millions of different
# colors, and we've named just a few here.
# In modern electronics, colors are formed by combining red, green, and blue
# lights in different proportions. Those proportions are expressed in software
# usually as numbers going from 0 (least color, darkest) to 255 (most color,
# lightest).
# I've expressed the colors above as a Python "dictionary": Dictionaries let
# you set a term and a definition for easy reference throughout a program's
# life.
# What this means is that rather than remembering that purple is expressed as
# (255, 0, 255), we can instead just remember the name 'purple'.


prompt = 'Ask a question and shake me up!'
# This little piece of text, called a "string", is what you'll see on the
# display when you start the program.
# Anytime you want to store text for display or for writing somewhere, you'll
# very likely use a string. When you let Python know that something is a
# string, you enclose it in quotation marks. You normally use single-quotes ('')
# when enclosing a string, but you'll need to use double-quotes ("") if your
# string itself has a single quote, like in the word "don't".


answers = [
    'But of course!',
    'Heavens, no!',
    'Definitely!',
    "Don't know, don't care.",
    "I don't know about that, but I do know it's %s degrees in here now."
]
# These are the insightful answers that our magic 8-ball can display after
# being shaken!
# These are answers are stored as "strings" in a Python "list". Each item in the
# list is separated by a comma, just like it is in English:
#    "Please bring back eggs, milk, and sugar."
# 
# If you add new answers, make sure there's a comma after the previous one.
#
# The last answer has a funny bit in it: "%s". This is a special Python
# placeholder for a part of the string that we don't know about right now, but
# will fill in later. This saves us from having to put the whole string together
# again; instead, we can just set the missing data right in place at the time we
# get it.


scroll_speed = 0.03
# Adjust this number to change how quickly the text scross by on the Sense Hat.
# Lower values are smaller! In my use, 0.06 worked out pretty well for
# demonstration.


sense = SenseHat()
# This gives Python an actual Sense Hat interface to use. If you thought that we
# already had this, let me offer this analogy: Using
#   "from sense_hat import SenseHat" 
# is like remembering to put the hammer and screwdriver in your toolbelt before
# you go to work, and using 
#   "sense = SenseHat()"
# is like actually having it in your hand. Why this works in this manner is a
# more advanced subject, however.


sense.show_message(prompt,
                   scroll_speed=scroll_speed)
# Here, we display the message on the Sense Hat's screen by telling the
# Sense Hat to do a trick called "show_message". In progamming languages, these
# "tricks" are called "functions". At the time we call this function, we 
# also specify the scrolling speed.


while True:
# This is the meat of the program. We set it up by telling Python to enter a 
# continuous loop with "while True". The instruction
#     "while XYZ:"
# tells Python: "keep doing what I'm about to tell you to do, but only as long
#                as XYZ holds true. When XYZ is not true anymore, stop doing 
#                it."
# The word "True" with a capital "T" is a Python shorthand for a generic true
# statement that will always be true, so this is an infinite loop!
# Can you think of a Python shorthand for a statement that will never be true?

    x, y, z = sense.get_accelerometer_raw().values()
    x = abs(x)
    y = abs(y)
    z = abs(z)
    # This determines how much how much acceleration the Sense Hat is currently
    # experiencing on each of its three axes: the X, Y, and Z axes. A positive
    # value indicates clockwise acceleration about an axis, and a negative
    # number is counterclockwise acceleration. Since we don't care about what
    # direction it's rotating and only how much it's rotating, we take the
    # absolute value of X, Y, and Z.

    x_threshold = 2
    y_threshold = 2
    z_threshold = 2
    if x > x_threshold and y > y_threshold and z > z_threshold:
        # This part might need some adjustment when you hook it up to your
        # own Sense Hat. Smaller numbers will make the magic 8-ball more
        # sensitive, and larger numbers make it less sensitive. Try it out with
        # various values and see what works for you.

        answer = choice(answers)
        # We pick an answer randomly from the set of answers we defined at the
        # start of the program.

        if 'degrees' in answer:
        # One special answer the magic 8-ball gives will include the real
        # temperature!...or so Sense Hat says. Since only in this case do we 
        # do something special other than just displaying our pre-written
        # answers, we introduce a conditional statement: "if".
        # Here, Python will see if the word "degrees" is in the answer that
        # was randomly chosen. If it is, we know that we're supposed to fill
        # in the temperature in our answer.
            celsius = int(sense.get_temperature_from_humidity())
            # This gets the temperature from the Sense Hat. Evidently it uses
            # humidity to determine this...so it might not be too accurate.

            fahrenheit = (celsius * 9/5) + 32
            # Of course, the temperature we get from the Sense Hat is in
            # Celsius, because the Sense Hat people are scientific types, and
            # all they do is in metric. We convert to Fahrenheit here.

            answer = answer % fahrenheit
            # Remember that funny placeholder "%s" from above? We'll use just
            # the "%" character this time to tell Python that we want to replace
            # "%s" with the degrees fahrenheit we just calculated.

        else:
        # This is a counterpart to the "if" statement above, which tells what
        # to do in other cases.
        #    "If the word 'degrees' is in the answer, do all this fancy stuff."
        #    "Otherwise..."
            pass
            #    "...do nothing."
            # If you don't specify an "else" statement, Python will assume
            # that you don't want anything to occur if the "if" statement
            # doesn't apply.

        sense.show_message(answer,
                           scroll_speed=scroll_speed,
                           text_colour=colors['white'],
                           back_colour=colors['black'])
        # At last, we show the answer to the question. We'll call the same 
        # function "show_message", but this time also specify the text and
        # background colors. Note how the colors, as specified here, relate
        # to the "colors" we specified at the beginning of our program. When
        # you want to refer to data stored in a dictionary, we use brackes ([])
        # and the name under which we stored our data.
    else:
    # If we didn't detect adequate acceleration,
        sense.clear()
        # ...just make sure nothing's displayed on the Sense Hat by issuing the
        # "clear" function.

# That's it! Feel free to explore by changing the values of some of the things
# we've set up here, like the colors, answers, and sensitivity.