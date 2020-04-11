import random
import sys
import copy
random.seed(None)
class Fish:
     species = None
     age = None
     hungry =None
     def __init__(self, species, age, hungry):
        self.species = species
        self.age = age
        self.hungry = hungry

     def prey_reproduce(self,species):
         self.species = species
         self.age = 1
         self.hungry =2

     def shark_eat_fish(self):
         self.species = 0
         self.age = 0
         self.hungry = 0

     def die(self):
         self.species = 0
         self.age = 0
         self.hungry = 0
class RandomCreature :
     play_board = []
     width = 10
     height = 10

     def __init__(self):
         #number_of_fish = 0
         #number_of_shark = 0
         #empty = 0
         #print("In the function")
         for row in range(10):
             row = []
             for column in range(10):
                 i = random.randint(0, 10)
                 #Age Random
                 j = random.randint(0,20)
                 #print(i)
                 #Empty
                 #%20 empty
                 if i<2:
                     row.append(Fish(0,0,0))
                     #empty+=1
                #Fish
                #%60 fish
                 elif 2<=i<8 :
                     row.append(Fish(1,j,2))
                     #number_of_fish+=1
                #Shark
                #%20 shark
                 elif i>=8:
                     row.append(Fish(2,j,2))
                     #number_of_shark+=1
             self.play_board.append(row)


     def calculatePopulation(self):
         collect = []
         empty = 0
         number_of_shark = 0
         number_of_fish = 0
         total_age_shark = 0
         total_age_fish = 0
         pb = self.play_board
         for i in range(10):
             for j in range(10):
                 if pb[i][j].species == 0:
                     empty +=1
                 elif pb[i][j].species == 1:
                     number_of_fish+=1
                     total_age_fish +=pb[i][j].age
                 elif pb[i][j].species == 2:
                     number_of_shark+=1
                     total_age_shark+=pb[i][j].age

         print('Shark: ', number_of_shark)
         print('Fish: ', number_of_fish)
         print('Empty: ', empty)

         collect.append(number_of_shark)
         collect.append(number_of_fish)
         collect.append(total_age_shark/number_of_shark)
         collect.append(total_age_fish/number_of_fish)

         return collect
     def showCreature(self):
            #print("Play Board",len(self.play_board))

            return self.play_board


     def turn(self):
         pb = self.play_board

         for i in range(10):
             for j in range(10):
                 self.getSpecies(i,j,pb[i][j])


     def getSpecies(self,x,y,fishShark):
         if fishShark.species == 0:
             print("*Empty*")
             return
         elif fishShark.species == 1 :
             print("*Fish*")
             neighbors = self.get_neighbors(x, y)
             shark = []
             fish = []
             empty = []
             if fishShark.age >=10:
                 print("Age")
                 fishShark.die()

             for i in neighbors :
                 #print("neighbors fish",i)
                 if i.species == 0:
                     empty.append(i)
                 elif i.species == 1 :
                     fish.append(i)
                 elif i.species ==2 :
                     shark.append(i)
              #Fish Rules
             if len(fish) >= 4:
                 print("Too much fish in the " , x ,y )
                 count =0
                 for j in fish:
                     if j.age >=2 :
                         count +=1
                 if count >=3 and len(empty)>0 :
                     print("Baby fished has been borned!",x,y)
                     print("Place",empty[random.randint(0, (len(empty))-1)])
                     empty[random.randint(0, (len(empty))-1)].prey_reproduce(1)




             if len(shark) < 4 and len(empty)>0 :
                 print("Shark has been borned",x,y)
                 print("Place",empty[random.randint(0, (len(empty))-1)])
                 empty[random.randint(0, (len(empty))-1)].prey_reproduce(2)


             elif len(shark)>=5 and len(fish)>0:
                 print("EAT!!")
                 targetFish = fish[random.randint(0, (len(fish)-1))]
                 targetFish.shark_eat_fish()

                 #print("Species become : " ,targetFish.age)

             elif len(fish) == 8:
                  print("Die!",x,y)
                  targetFish = fish[random.randint(0, (len(fish)-1))]
                  targetFish.die()


             fishShark.age +=1
             return
             #print("Neighbors fish",fish.age)
             #print("Neighbors shark", shark)
             #print("Neighbors empty", empty)
         elif fishShark.species ==2 :
             print("*Shark*")
             neighbors = self.get_neighbors(x, y)
             shark = []
             fish = []
             empty = []
             if fishShark.age >=20:
                 print("AgeShark")
                 fishShark.die()

             for i in neighbors :
                 #print("neighbors fish",i)
                 if i.species == 0:
                     empty.append(i)
                 elif i.species == 1 :
                     fish.append(i)
                 elif i.species ==2 :
                     shark.append(i)

              #Shark Rules
             random_death = random.randint(0,1000)
             if len(shark) >= 4:
                 print("Too much shark in the " , x ,y )
                 count =0
                 for j in shark:
                     if j.age >=3 :
                         count +=1
                 if count >=3 and len(empty)>0:
                     empty[random.randint(0, (len(empty))-1)].prey_reproduce(2)

                     print("Baby shark has been borned!",x,y)


             if len(fish) < 4  and len(empty)>0 :
                 print("Fish has been borned",x,y)
                 empty[random.randint(0, (len(empty))-1)].prey_reproduce(1)


             elif (len(shark) >=6 and len(fish) == 0) or random_death <=31 :
                  print("Shark die",x,y)
                  targetShark = shark[random.randint(0, (len(shark)-1))]
                  targetShark.die()

             fishShark.age +=1
             return

     def get_neighbors(self, x, y):
          top = self.play_board[x][(y - 1) % self.height]
          tr = self.play_board[(x + 1) % self.width][(y - 1) % self.height]
          right = self.play_board[(x + 1) % self.width][y]
          br = self.play_board[(x + 1) % self.width][(y + 1) % self.height]
          bottom = self.play_board[x][(y + 1) % self.height]
          bl = self.play_board[(x - 1) % self.width][(y + 1) % self.height]
          left = self.play_board[(x - 1) % self.width][y]
          tl = self.play_board[(x - 1) % self.width][(y - 1) % self.height]

          neighbors = [top, tr, right, br, bottom, bl, left, tl]
          return neighbors
