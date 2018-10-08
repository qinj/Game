import random


class Room():
    def __init__(self, name, desc):
        self.name = name
        self.roomDict = {}
        self.desc = desc
        self.treasList = []

    def __str__(self):
        return self.name + ": " + self.desc

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getDesc(self):
        return self.desc

    def setDesc(self, desc):
        self.desc = desc

    def setNext(self,dir,room):
        self.roomDict[dir] = room

    def getNext(self, dir):
        return self.roomDict[dir]

    def getRooms(self):
        return self.roomDict

    def setRooms(self, roomDir):
        self.roomDict = roomDir

    def getTreasure(self):
        return self.treasList

    def addTreasure(self, theTreasure):
        self.treasList.append(theTreasure)

    def setTreasure(self, treasure):
        self.treasList = treasure

    def isRoomInDir(self, dir):
        return dir in self.roomDict


class Player():
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.numLives = int(3)
        self.treasList = []

    def getPoints(self):
        # return the total points from my list of treasure

        getTreasPoints = 0
        for treas in self.treasList:
            getTreasPoints = getTreasPoints +  treas.getTreasPoints()
        return getTreasPoints

    def setRoom(self,theRoom):
       self.currentRoom = theRoom

    def getRoom(self):
       return self.currentRoom

    def getTreasure(self):
        return self.treasList

    def setTreasure(self, treasure):
        self.treasList = treasure

    def getLives(self):
        return self.numLives

    def setLives(self, num):
        self.numLives = num

    def addTreasure(self, RmTreaList):
        for tr in RmTreaList:
            self.treasList.append(tr) #add room treasure to player treasure list
        RmTreaList.clear() #clears treasure from room


class Treasure():
    def __init__(self, treasName, treasDesc, treasPoints):
        self.treasName = treasName
        self.treasDesc = treasDesc
        self.treasPoints = treasPoints

    def setTreasName(self, treasName):
        self.treasName = treasName

    def getTreasName(self):
        return self.treasName

    def setTreasDesc(self, treasDesc):
        self.treasDesc = treasDesc

    def getTreasDesc(self):
        return self.treasDesc

    def setTreasPoints(self, treasPoints):
        self.treasPoints = treasPoints

    def getTreasPoints(self):
        return self.treasPoints


class Game():
    def __init__(self):

        # create the rooms
        r1 = Room("Room 1", "The room is very big")
        r2 = Room("Room 2", "It's kind of cold in here")
        r3 = Room("Room 3", "It is hot in here")
        r4 = Room("Room 4", "You should get out of here ASAP")
        r5 = Room("Room 5", "There's no way you can leave this room")
        r6 = Room("Room 6", "All the walls are painted blue")
        r7 = Room("Room 7", "There's a lot of small rabbits in this room")
        r8 = Room("Room 8", "This room is very small")
        r9 = Room("Room 9", "The room is full of light")

        # create the dictionary of direction and next room
        #    - r1
        # r2 - r3
        # r4 - r5 - r6
        # r7 - r8
        #    - r9
        r1.setRooms({'s':r3})
        r2.setRooms({'e':r3, 's': r4})
        r3.setRooms({'s':r5, 'w': r2, 'n':r1})
        r4.setRooms({'n':r2, 'e':r5, 's': r7})
        r5.setRooms({'w':r4, 'e':r6, 'n': r3, 's': r8})
        r6.setRooms({'w':r5})
        r7.setRooms({'n': r4, 'e': r8})
        r8.setRooms({'n': r5, 'w': r7, 's': r9})
        r9.setRooms({'n': r8})

        # set my start (r1) and end room (r9)
        self.start = r1
        self.end = r9

        # create the treasure and add it to the rooms (some rooms have no treasures)
        t1 = Treasure("Lamp", "A shiny gold lamp", 20)
        t2 = Treasure("Watch", "An old pocket watch", 30)
        t3 = Treasure("Stone", "A flowing stone", 20)
        t4 = Treasure("Necklace", "A gold necklace with sparkling stones", 50)
        t5 = Treasure("Book", "A hardcover book with gold letters", 20)
        t6 = Treasure("Necklace", "A gold necklace with sparkling stones", 50)
        t7 = Treasure("Book", "A gold cube", 60)
        # r1.addTreasure(t1)
        # r2.addTreasure(t2)
        # r3.addTreasure(t3)
        # r4.addTreasure(t4)
        # r5.addTreasure(t5)

        #add treasure to random room
        tList = [t1, t2, t3, t4, t5, t6, t7]
        for t in tList:
            randRoom_No= random.randint(1,10)
            if randRoom_No == 1:
                r1.addTreasure(t)
            elif randRoom_No == 2:
                r2.addTreasure(t)
            elif randRoom_No == 3:
                r3.addTreasure(t)
            elif randRoom_No == 4:
                r4.addTreasure(t)
            elif randRoom_No == 5:
                r5.addTreasure(t)
            elif randRoom_No == 6:
                r6.addTreasure(t)
            elif randRoom_No == 7:
                r7.addTreasure(t)
            elif randRoom_No == 8:
                r8.addTreasure(t)
            elif randRoom_No == 9:
                r9.addTreasure(t)

    def getStart(self):
        return self.start

    def setStart(self, start):
        self.start = start

    def getEnd(self):
        return self.end

    def setEnd(self, exit):
        return self.end

    def play(self):
        p1 = Player(self.getStart()) #create player at start room

        while p1.getPoints() < 100 or p1.getLives() >= 1:
            print(str(p1.getRoom()))
            room = p1.getRoom()
            treasureList = room.getTreasure()

            for t in treasureList:
                t_desc = t.getTreasDesc()
                print(t_desc)

            p1.addTreasure(treasureList) #moves room treasure to player's list
            # direction = ''
            # while True:
            direction = input('Which direction would you like to go? (n, e, s, w)') #prompt player which direction to go
            # if direction != "n" and direction != "e" and direction != "w" and direction != "s":
            #     # print("Not a direction. Choose n, e, s, or w.")

            if direction in room.getRooms().keys(): #if direction is in keys of roomDict (valid direction)
                roomDict = room.getRooms()
                if roomDict[direction] == self.getEnd(): #check if room moving to is exit room
                    if p1.getPoints() >= 100: #check if have enough points to win
                        print("You have won!")
                        exit()
                #if line 214 not true (i.e. not enough points to win)- continue to line below/keep playing
                p1.setRoom(roomDict[direction]) #updates player's current room


            else:
                player_lives = p1.getLives()
                player_lives = player_lives - 1 #take away 1 life if direction isn't valid
                p1.setLives(player_lives) #update players remaining lives

playGame = Game()
playGame.play()