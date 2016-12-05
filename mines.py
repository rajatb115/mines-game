import pygame
import random

pygame.init()

def mine(n,bombs):  #create the matrix that will use us in the future
	table = create_table(n)
	table = add_bombs(table,bombs)
	table = change_table(table)
	return table


def create_table(n):
	return [[0] * n for i in range(n)]  #this will return a 2d array ,if n=3 then array will be [0,0,0][0,0,0][0,0,0] 


def add_bombs(table,bombs):
	for i in range(bombs):
		is_bomb = False
		while not is_bomb:
			x = random.randrange(0,len(table)-1)
			y = random.randrange(0,len(table)-1)
			if table[x][y] != 9:  # here 9 is used as a reference that this place contain bomb
				table[x][y] = 9
				is_bomb = True
	return table



def change_table(table):  #to change number around bombs
	for x in range(0,len(table)):  # this will give the no of rows in the table or sa array
		for y in range(0,len(table)):  #this will give the no of colums in the particular row of the table
			if table[x][y] == 9:
				#pri(table)
				table = check_down_left(table,x,y)
				#pri(table)
				table = check_down_right(table,x,y)
				#pri(table)
				table = check_down(table,x,y)
				#pri(table)
				table = check_up_left(table,x,y)
				#pri(table)
				table = check_up_right(table,x,y)
				#pri(table)
				table = check_up(table,x,y)
				#pri(table)
				table = check_left(table,x,y)
				#pri(table)
				table = check_right(table,x,y)
				#pri(table)
	return table


def check_down_left(table,x,y): # checks whether this portion is counted for the non bomb 
	if x - 1 >= 0 and y + 1 < len(table): #changed from real code
		if table[x-1][y+1] != 9:
			table[x-1][y+1] = table[x-1][y+1] + 1
	return table


def check_down_right(table,x,y):
	if x + 1 < len(table) and y + 1 < len(table): #changed from real code
		if table[x+1][y+1] != 9:
			table[x+1][y+1] = table[x+1][y+1] + 1
	return table

def check_down(table,x,y):
	if y + 1 < len(table): #changed from real code
		if table[x][y+1] != 9:
			table[x][y+1] = table[x][y+1] + 1
	return table

def check_up_left(table,x,y):
	if x - 1 >= 0 and y - 1 >= 0: #changed from real code
		if table[x-1][y-1] != 9:
			table[x-1][y-1] =table[x-1][y-1] + 1
	return table

def check_up_right(table,x,y):
	if x + 1 < len(table) and y - 1 >=0: #changed from real code
		if table[x+1][y-1] != 9:
			table[x+1][y-1] = table[x+1][y-1] + 1
	return table
	
def check_up(table,x,y):
	if y - 1 >= 0: #changed from real code
		if table[x][y-1] != 9:
			table[x][y-1] =table[x][y-1] + 1
	return table
	
def check_right(table,x,y):
	if x + 1 < len(table): #changed from real code
		if table[x+1][y] != 9:
			table[x+1][y] =table[x+1][y] + 1
	return table

def check_left(table,x,y):
	if x - 1 >= 0 : #changed from real code
		if table[x-1][y] != 9:
			table[x-1][y] =table[x-1][y] + 1
	return table
	
def pri(table):
	for i in table:
		print(i)



###############################################################
############# NOW GRAPHICS OPTION #############################


class Square:
	def __init__(self,x,y,w,h,board,i,j):
		self.rect=pygame.rect.Rect(x,y,w,h)
		self.i=i
		self.j=j
		self.val=board[i][j]
		self.x=x
		self.y=y
		self.visible=False
		self.flag=False


def open_game(lst,size,xx,yy,numbers,screen):
	screen.blit(numbers[lst[xx][yy].val],(xx*50,yy*50))
	lst[xx][yy].visible=True
	pygame.display.flip()
	if lst[xx][yy].val == 0:
		#print("yes")

		if yy > 0:
			if lst[xx][yy-1].visible==False and lst[xx][yy-1].val < 9 :
				open_game(lst,size,xx,yy-1,numbers,screen)
		if xx + 1 < size and yy > 0:
			if lst[xx+1][yy-1].visible==False and lst[xx+1][yy-1].val < 9 :
				open_game(lst,size,xx+1,yy-1,numbers,screen)
		if xx > 0 and yy > 0:
			if lst[xx-1][yy-1].visible==False and lst[xx-1][yy-1].val < 9 :
				open_game(lst,size,xx-1,yy-1,numbers,screen)
		if xx > 0:
			if lst[xx-1][yy].visible==False and lst[xx-1][yy].val < 9  :
				open_game(lst,size,xx-1,yy,numbers,screen)
		if xx+1 < size:
			if lst[xx+1][yy].visible==False and lst[xx+1][yy].val < 9 :
				open_game(lst,size,xx+1,yy,numbers,screen)
		if yy+1 < size:
			if lst[xx][yy+1].visible==False and lst[xx][yy+1].val < 9 :
				open_game(lst,size,xx,yy+1,numbers,screen)
		if yy+1 < size and xx+1 < size:
			if lst[xx+1][yy+1].visible==False and lst[xx+1][yy+1].val < 9 :
				open_game(lst,size,xx+1,yy+1,numbers,screen)
		if yy+1 < size and xx >0:
			if lst[xx-1][yy+1].visible==False and lst[xx-1][yy+1].val < 9:
				open_game(lst,size,xx-1,yy+1,numbers,screen)


def game_won(size,lst,bombs):
	count = 0
	for i in range(size):
		for j in range(size):
			if lst[i][j].val==9 and lst[i][j].flag==True:
					count=count+1
	if count==bombs:
		print("game won")
		run=False


def game_start(size,bombs):
	
	grey=pygame.image.load('grey_50_50.png')
	white=pygame.image.load("white_50_50.png")
	zero=pygame.image.load("white_50_50.png")
	one=pygame.image.load("one.png")
	two=pygame.image.load("two.png")
	three=pygame.image.load("three.png")
	four=pygame.image.load("four.png")
	five=pygame.image.load("five.png")
	six=pygame.image.load("six.png")
	seven=pygame.image.load("seven.png")
	eight=pygame.image.load("eight.png")
	nine=pygame.image.load("mine_50_50.png")
	redb=pygame.image.load("bomb_50_50.png")
	Flag=pygame.image.load("flag_50_50.png")


	tables=mine(size,bombs)
	pri(tables)

	w = size*50
	h = size*50


	screen=pygame.display.set_mode((a*50,a*50))
	pygame.display.set_caption('Mines')

	numbers=[zero,one,two,three,four,five,six,seven,eight,nine]

	lst=[[0]*size for i in range(size)]
	for i in range(0,size):
		for j in range(0,size):
			lst[i][j]= Square(i*50,j*50,50,50,tables,i,j)
			screen.blit(grey,(i*50,j*50))
			pygame.display.flip()

	run=True


	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False
				pygame.quit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					run=False
					#print("r")
					pygame.quit()
					game_start(size,bombs)

			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				#print("yes")
				#for i in lst:
					#for j in i:
						#print(j)
						#r=pygame.rect.Rect(pygame.mouse.get_pos(),(1,1))
						#r=pygame.mouse.get_pos()
						#print(r)
				r=pygame.mouse.get_pos()
				#print(r)
				xx=r[0]//50
				yy=r[1]//50
				if lst[xx][yy].flag == False and lst[xx][yy].visible == False:
					#print("False flag")
					#print(lst[xx][yy].val)
					if lst[xx][yy].val == 9 :
						print("GAME OVER")
						#run = False
						screen.blit(redb,(xx*50,yy*50))
						pygame.display.flip()
						lst[xx][yy].visible = True

						for i in range(size):
							for j in range(size):
								#lst[i][j].visible = True
								if lst[i][j].val == 9:
									if lst[i][j].flag == False and lst[i][j].visible == False:
										screen.blit(nine,(i*50,j*50))
										pygame.display.flip()

										#font = pygame.font.Font(None, 36)
										#text = font.render("Press 'r' to play again", 1, (255, 0, 0))
			
										#screen.blit(text,((size*50/2)-125,size*50/2))
										#pygame.display.flip()

										#for event1 in pygame.event.get():
											#if event1.type == pygame.KEYDOWN:
												#if event1.key == pygame.K_r:
													#run=False
													#print("r")
													#pygame.quit()
													#game_start(size,bombs)
						for i in range(size):
							for j in range(size):
								lst[i][j].visible = True


					else:
						if lst[xx][yy].val != 0:
						 	screen.blit(numbers[lst[xx][yy].val],(xx*50,yy*50))
						 	lst[xx][yy].visible=True
						 	pygame.display.flip()
						elif lst[xx][yy].val == 0:
							open_game(lst,size,xx,yy,numbers,screen)


			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
				r=pygame.mouse.get_pos()
				xx=r[0]//50
				yy=r[1]//50
				#if lst[xx][yy].visible==False:
				if lst[xx][yy].flag==False:
					if lst[xx][yy].visible==False:
						lst[xx][yy].flag=True
						#lst[xx][yy].visible=True
						screen.blit(Flag,(xx*50,yy*50))
						pygame.display.flip()
						game_won(size,lst,bombs)


				#if lst[xx][yy].visible==True:
				elif lst[xx][yy].flag==True:
					if lst[xx][yy].visible==False:
						lst[xx][yy].flag=False
						#lst[xx][yy].visible=False
						screen.blit(grey,(xx*50,yy*50))
						pygame.display.flip()


				#print("button 3")
				#rr=pygame.mouse.get_pos()
				#xx=rr[0]//50
				#yy=rr[1]//50 
				#if lst[xx][yy].visible == False:
                    #if lst[xx][yy].flag == False:
                        #lst[xx][yy].flag = True
                        #lst[xx][yy].visible=True
                    #elif lst[xx][yy].flag == True:
                        #lst[xx][yy].flag = False
                        #lst[xx][yy].visible=False


    


####################################################################
############# INPUT ################################################

a=input("enter no. of blocks :: ")
b=(a*a)//6
#table=mine(a,b)
#pri(table)
game_start(a,b)