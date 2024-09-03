import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

distances = {}
positions = {}


# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    i = 0  # Compteur de changement de checkpoint
    j = 0  # Compteur pour le boost, j'ai pas de façon intelligente de l'utiliser pour le moment

    if i == 0:
        distances[i] = next_checkpoint_dist
        positions[i] = (next_checkpoint_x, next_checkpoint_y)

        i += 1
    elif i > 0 and positions[i] != positions[i-1]:
        distances[i] = next_checkpoint_dist
        positions[i] = (next_checkpoint_x, next_checkpoint_y)

        i +=1
    
    thrust = 100
    distance_restante = next_checkpoint_dist/distances[i-1]
    x = 1 - distance_restante

    thrust_proche_checkpoint = 0.01 # Accélération quand on arrive (très) proche d'un checkpoint
    coupure = 1/2 # Instant de changement de régime (compris entre 0 et 1)

    b = - math.log(thrust_proche_checkpoint)
    a = (1/coupure)*b

    regime_1 = 1
    regime_2 = math.exp(-a*x+b)

    coeff = min(regime_1, regime_2)

    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        coeff = 0

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100) or "BOOST"
    # i.e.: "x y thrust"

    if j == 0 and next_checkpoint_angle == 0:
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " BOOST")
        j += 1
    else:
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " +str(int(coeff * thrust)))