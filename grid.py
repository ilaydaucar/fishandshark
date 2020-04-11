import pygame
import FishAndShark
import sys
import matplotlib.pyplot as plt
import pandas as pd


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5

color_arr = [WHITE, GREEN, RED]


pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Fish - Shark")
pp =FishAndShark.RandomCreature()
clock = pygame.time.Clock()

def paint(x, y, color_int):
    pygame.draw.rect(screen,
                     color_arr[color_int],
                     [(MARGIN + WIDTH) * x + MARGIN,
                      (MARGIN + HEIGHT) * y + MARGIN,
                      WIDTH,
                      HEIGHT])

def paint_map(board):
    pa = paint
    length = len(board)

    for x in range(0, length):
        for y in range(0, length):
            #print(x*5,y*5)
            pa(x, y, board[x][y].species)
count = 0
population_number = 0
number_of_shark = []
number_of_fish = []
generation = []
average_age_shark = []
average_age_fish =[]

font = {'family': 'serif',
        'color':  'black',
        'weight': 'bold',
        'size': 12,
        }
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_stopped = True

            print(len(generation))
            print(len(number_of_shark))
            df=pd.DataFrame({'Generation': generation, 'Shark': number_of_shark , 'Fish' : number_of_fish })
            df2=pd.DataFrame({'Generation': generation,'Shark':average_age_shark,'Fish':average_age_fish })
            #Population
            plt.plot( 'Generation', 'Shark', data=df, marker='', color='red', linewidth=2)
            plt.plot( 'Generation', 'Fish', data=df, marker='', color='green', linewidth=2)
            plt.xlabel("Generation",fontdict=font)
            plt.ylabel("Population",fontdict=font)
            plt.title("Fish-Shark Population Plot",fontdict=font)
            plt.legend()
            plt.savefig('population.png')
            plt.show()

            #AverageAge
            print("Average Shark Age",average_age_shark)
            print("Average Fish Age", average_age_fish)
            plt.plot( 'Generation', 'Shark', data=df2, marker='', color='red', linewidth=2)
            plt.plot( 'Generation', 'Fish', data=df2, marker='', color='green', linewidth=2)
            plt.xlabel("Generation",fontdict=font)
            plt.ylabel("Average Age",fontdict=font)
            plt.title("Fish-Shark Average Age Plot",fontdict=font)
            plt.legend()
            plt.savefig('average_age.png')
            plt.show()



            sys.exit(0)
    print("*Creature is creating*")
    paint_map(pp.showCreature())
    population_number = pp.calculatePopulation()

    number_of_shark.append(int(population_number[0]))
    number_of_fish.append(int(population_number[1]))
    average_age_shark.append(int(population_number[2]))
    average_age_fish.append(int(population_number[3]))
    generation.append(int(count))
    count +=1
    clock.tick(60)
    pygame.display.flip()
    #pygame.image.save(screen, "frame-%03d.png" % (count))
    pp.turn()
    #print("Number of Shark",number_of_shark)
    #print("Number of Fish", number_of_fish)
