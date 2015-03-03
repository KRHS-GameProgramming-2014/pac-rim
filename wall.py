import pygame, math, sys, time, os
from playerKaiju import PlayerKaiju
from enemyJaeger import EnemyJaeger

class Block():
	def __init__ (self, image, pos, sizee):
		self.baseImage = pygame.image.load(image)
		if size != None:
			self.resize(size)
		else:
			self.image = self.baseImage
		self.rect = self.image.get_rect()
		self.place(pos)
	def place(self, pos):
		self.rect.center = pos
		
	def resize (self, size):
		self.image = pygame.transform.scale(self.baseImage, size)
		
	def distance(self, pt):
		x1 = self.rect.center[0]
		y1 = self.rect.center[0]
		y2 = pt[0]
		x2 = pt[0]
		return math.sqrt (((x2-x1)**2) + ((y2-y1)**2))
		
	def playerCollide(self, other):
		if (self.rect.right > other.rect.left
			and self.rect.left < other. rect.right):
			if (self.rect.bottom > other.rect.top and
				self.rect.top < other.rect.bottom):
				return True
		return False
		
	def jaegerCollide(self, other):
		if (self.rect.right > other.rect.left
			and self.rect.left < other.rect.right):
			if (self.rect.bottom > other.rect.top and
				self.rect.top < other.rect.bottom):
				#print "Collide With: ", other
				return True
		return False
				
	def update(self):
		pass


class Level():
    def __init__(self, level, names, screenSize):
        self.screenSize = screenSize
        self.names = names
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.blocks = []
        self.hardBlocks = []
        
        #self.levelChangeBlocks = []
        #self.ghosts = []
        
        self.players = []
        
        self.blockSize = 64
        self.level = level
        self.load(level)
        

    def killOldLevels(self, timeInSeconds):
        for f in os.listdir("RSC/Maps/"):
            if f[-5:] == ".tngs":
                print f, time.time() - os.path.getmtime("RSC/Maps/"+f), timeInSeconds
                if (time.time() - os.path.getmtime("RSC/Maps/"+f)) > timeInSeconds:
                    print f
                    os.remove("RSC/Maps/"+f)
            
    """
    def unload(self):
        things = []
        line = []
        for y in range(14):
            for x in range(20):
                line += [" "]
            things += [line]
            line = []
        #print len(things), len(things[0])
        
        for ghost in self.ghosts:
            things[ghost.rect.center[1]/50][ghost.rect.center[0]/50] = "G"
        for lc in self.levelChangeBlocks:
            things[lc.rect.center[1]/50][lc.rect.center[0]/50] = lc.kind
        
        thingString = ""
        for line in things:
            for c in line:
                thingString += c
            thingString += "\n"
        #print thingString
        
        thingMap="RSC/Maps/"+ self.level +".tngs"
        savedThingfile = open(thingMap, "w")
        savedThingfile.write(thingString)
        savedThingfile.close()
            
        while len(self.blocks) > 0:
            self.blocks.remove(self.blocks[0])
        while len(self.hardBlocks) > 0:
            self.hardBlocks.remove(self.hardBlocks[0])
        while len(self.levelChangeBlocks) > 0:
            self.levelChangeBlocks.remove(self.levelChangeBlocks[0])
        while len(self.ghosts) > 0:
            self.ghosts.remove(self.ghosts[0])
	"""
	
    def load(self, level):  
        self.level = level
        print self.level
        geoMap="RSC/Maps/"+ level +".lvl"
        thingMap="RSC/Maps/"+ level +".tng"

        geofile = open(geoMap, "r")
        lines = geofile.readlines()
        geofile.close()
        newlines = []
        

        #Clean up the file by stripping newlines!
        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]

        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
                if c == "#":
                    self.hardBlocks += [Block("RSC/Block/bush.png",
                                    [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                    (self.blockSize,self.blockSize))]
                    self.blocks += [self.hardBlocks[-1]]
                if c == "*":
                    self.blocks += [Block("RSC/Block/block.png",
                                    [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                    (self.blockSize,self.blockSize))]

        
        thingfile = open(thingMap, "r")
        lines = thingfile.readlines()
        thingfile.close()

        newlines = []

        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]

        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
#-------Blocks  
                if c == "@":
                    if len(self.players) == 0:
                        if len(self.names) > 0:
                            daName = self.names.pop()
                            self.players += [Player(daName,  [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
				#if c == "G":
                #    self.ghosts += [Ghost(
                #                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
