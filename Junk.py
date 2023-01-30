# hw1_fns
# Demonstrate functions and calculations in Python
#
# This program asks for a resistance (ohms) and calculates
# the current and power for 5 V and 3.3 V applied to the
# resistor using a function.
#
# Notice that most programming languages refer to real
# numbers as "floating point" or "float".  For scientific
# calculations, a version called "double precision" or "double"
# is often used to obtain a greater range and more significant
# figures, but "float" is adequate for this application.
#
# You may create your own functions using those below as models.
# Functions let you re-use a procedure in different ways,
# saving a lot of typing and memory space.
#
# A function may return a value.  In Python, it may return multiple
# values.  Our examples don't return anything.
#
# The "while" statement performs the action following it
# as long as its condition is true.  When the condition becomes
# false, the "while" statement repetition ends.
#
# USU Phys 3500
# 13 Jan 2022

# Calculate the power (milliwatts) given a voltage and resistance
# using P = V*I = V*(V/R)
# The values passed to the function are called "arguments" and
# must be defined as local variables with a type (float, int,
# etc.) and a name.  The name can be anything you like.
#
def JoulesLaw( V_volts, R_ohms ):

    P_watts = V_volts*V_volts/R_ohms
    print( f"{V_volts} V applied to {R_ohms} ohms dissipates {P_watts*1000.0} mW." )

# Calculate the current (milliamps) given a voltage and resistance
# using I = V/R
#
def OhmsLaw( V_volts, R_ohms ):

    I_amps = V_volts/R_ohms
    print( f"{V_volts} V applied to {R_ohms} ohms produces {I_amps*1000.0} mA." )

# Setup: print a title
print("Ohm's Law and Joule's Law Calculation")

# Loop: press Ctrl-C to kill the program
while True:  # loop forever
    R_ohms = float(input("\nEnter resistance value in ohms:  "))

    # do not trust users! be sure values make sense.
    if R_ohms < 0.0:
        print( "Your resistance is futile.  It must be positive." )
        continue

    # Calculate and display current through R for 3.3 V
    OhmsLaw( 3.3, R_ohms )
    # Calculate and display power dissipated by R for 3.3 V
    JoulesLaw( 3.3, R_ohms )
    # Calculate and display current through R for 5 V
    OhmsLaw( 5.0, R_ohms );
    # Calculate and display power dissipated by R for 5 V
    JoulesLaw( 5.0, R_ohms );
