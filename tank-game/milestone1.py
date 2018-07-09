#importing py game function
import pygame
import sys
import random
import time
#creating function in pygame
pygame.init()


#getting color
white =(255,255,255)
black =(0,0,0)
red = (138,0,0)
light_red= (255,0,0)

green =(0,138,0)
light_green= (0,255,0) 
blue =(0, 0, 255)
yellow = (138,138,0)
light_yellow= (255,255,0)
fire_red= (156, 42, 0)
orange_red= (255,69,0)
saddlebrown=(139,69,19)
burlywood=(222,184,135)
clock = pygame.time.Clock()
#setting up the display and snake coordinate
screen_width = 1000
screen_height = 600
fps =15
block_size = 15
apple_size= 15
size = (screen_width,screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('tank')
#icon = pygame.image.load('snakeup.png')
#pygame.display.set_icon(icon)

#bulding materials of tank
tankWidth= 40
tankHeight= 20
turretWidth= 5
wheelWidth= 5

#defining the size of font or text to display
smallfont = pygame.font.SysFont("Waree", 25)
medfont = pygame.font.SysFont("Purisa", 50)
largefont = pygame.font.SysFont("Purisa", 80)


#apple = pygame.image.load('apple.png')
#img = pygame.image.load('snakeup.png')
#img_body = pygame.image.load('snake_body.png')




#function for message to game
def text_objects(text, color,size):
	if size == 'small':
		textSurface = smallfont.render(text, True, color)
	if size == 'medium':
		textSurface = medfont.render(text, True, color)
	if size == 'large':
		textSurface = largefont.render(text, True, color)
	return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth,buttonheight, size= 'small'):
	textSurf, textRect = text_objects(msg,color,size)
	textRect.center = ((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
	screen.blit(textSurf, textRect)

def message_to_screen(mesg, color,y_displace=0, size='small'):
	textSurf, textRect= text_objects(mesg, color,size)
	#screen_text= font.render(mesg, True,color)
	#screen.blit(screen_text,[screen_width/5,screen_height/2])
	textRect.center = (screen_width/2) , (screen_height /2)+ y_displace
	screen.blit(textSurf, textRect)


#function for pause
def paused():
	paused= True
	message_to_screen("paused",black, -200, size='large')
	message_to_screen("Press C to continue and Q to quit",black, -100)
	pygame.display.update()
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						paused = False
					elif event.key == pygame.K_q:
						pygame.quit()
						quit()
		#screen.fill(white)
		clock.tick(5)

#function for score
def score(score):
	text= smallfont.render('score:' +str(score), True, black)
	screen.blit(text, [0,0])

	
	
	
#making a tank
def tank(x,y,turPos):
	x= int(x)
	y= int(y)
	
	
	possibleTurret =[(x-27,y-2),
					 (x-26,y-5),
					 (x-25,y-8),
					 (x-23,y-12),
					 (x-20,y-12),
					 (x-18,y-14),
					 (x-15,y-17),
					 (x-13,y-19),
					 (x-11,y-21),
					 #(x-9, y-23),
					
					]
	pygame.draw.circle(screen,saddlebrown, (x,y),int(tankHeight/2))
	pygame.draw.rect(screen, saddlebrown, (x-tankHeight,y ,tankWidth, tankHeight))
	pygame.draw.line(screen, saddlebrown, (x,y), possibleTurret[turPos],turretWidth)
	for x in range(x,x+35,5):
		pygame.draw.circle(screen, black,(x-15,y+20), wheelWidth)
	return possibleTurret[turPos]


def enemy_tank(x, y, turPos):
	x = int(x)
	y = int(y)

	possibleTurret = [(x + 27, y - 2),
					  (x + 26, y - 5),
					  (x + 25, y - 8),
					  (x + 23, y - 12),
					  (x + 20, y - 12),
					  (x + 18, y - 14),
					  (x + 15, y - 17),
					  (x + 13, y - 19),
					  (x + 11, y - 21),
					  # (x-9, y-23),

					  ]
	pygame.draw.circle(screen, black, (x, y), int(tankHeight / 2))
	pygame.draw.rect(screen, black, (x - tankHeight, y, tankWidth, tankHeight))
	pygame.draw.line(screen, black, (x, y), possibleTurret[turPos], turretWidth)
	for x in range(x, x + 35, 5):
		pygame.draw.circle(screen, black, (x - 15, y + 20), wheelWidth)
	return possibleTurret[turPos]
	
#controls function
def game_contrlos():
	gcont = True
	while gcont:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()	
		screen.fill(white)
		message_to_screen("Controls",green,-200, size='medium')
		message_to_screen("Fire: Spacebar",black,-150, size='small')
		message_to_screen("Move Turret: UP and DOWN arrows",black,-100, size='small')
		message_to_screen("Move Tank: Left and Right arrows",black,-50, size='small')
		message_to_screen("Pause: P",black,0, size='small')
		#putting buttons on screen
		
		button('play',(screen_width/2)-300,500,100,50, green, light_green, action='p')
		button('main',(screen_width/2)+50,500,120,50,yellow, light_yellow, action='m')
		button('quit',(screen_width/2)+350,500,100,50, red, light_red, action='q')
		
		pygame.display.update()
		clock.tick(5)
		

#button function/ creating buttons		
def button(text, x ,y ,width, height, inactive_color, active_color, action = None):
	cur= pygame.mouse.get_pos()
	click =pygame.mouse.get_pressed()
	
	if x+width > cur[0] > x and y+height > cur[1] >y:
		pygame.draw.rect(screen,active_color,(x,y,width,height))
		if click[0] == 1 and action != None:
			if action == 'q':
				pygame.quit()
				quit()
			if action == 'p':
				gameloop()
			if action == 'c':
				game_contrlos()
				#pass
			if action =='m':
				game_intro()
	else:
		pygame.draw.rect(screen,inactive_color,(x,y,width,height))
	text_to_button(text,black,x ,y ,width, height)
	#pygame.display.update()	

#defining explosion function
def explosion(x,y):
	explode = True
	while explode:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		startPoint= x,y
		cholorChoices=[light_yellow,fire_red, orange_red]
		magnitude=1
		while magnitude <30:
			#exploding_bit_x= x + random.randrange(-1*magnitude,magnitude)
			#exploding_bit_y = y + random.randrange(-1 * magnitude, magnitude)
			#pygame.draw.circle(screen,cholorChoices[random.randrange(0,3)],(exploding_bit_x,exploding_bit_y),random.randrange(2,6))
			pygame.draw.circle(screen,cholorChoices[random.randrange(0,3)],(x,y),magnitude)
			magnitude +=1
			pygame.display.update()
			clock.tick(60)
		explode =False


#creating function for firing

def fireshell(xy, ground_height, turpos, gun_power,xlocation, randomHeight, barrierWidth,eTankx,eTanky):
	damage= 0
	fire = True
	startingshell = list(xy)
	# print ("fire")
	while fire:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		# print(startingshell[0],startingshell[1])
		pygame.draw.circle(screen, fire_red, (startingshell[0], startingshell[1]), 5)
		

		startingshell[0] -= (12 - turpos) * 2
		startingshell[1] += int((((startingshell[0] - xy[0]) * 0.013/(gun_power/50)) ** 2) - (turpos + turpos / (12 - turpos)))
		# fire =False
		if startingshell[1] > screen_height-ground_height:
			hit_x= int((startingshell[0]*(screen_height-ground_height/2))/startingshell[1])
			hit_y = int(screen_height-ground_height)
			if eTankx+15> hit_x >eTankx-15:
				damage = 25
			explosion(hit_x, hit_y)
			fire = False

		check_x_1= startingshell[0] <= xlocation+barrierWidth
		check_x_2 = startingshell[0] >= xlocation

		check_y_1 = startingshell[1] >= screen_height- randomHeight
		check_y_2 = startingshell[1] <= screen_height
		if check_x_1 and check_x_2 and check_y_1 and check_y_2:
			hit_x = startingshell[0]
			hit_y = startingshell[1]
			explosion(hit_x, hit_y)
			fire = False


		pygame.display.update()
		clock.tick(100)
	return damage


def e_fireshell(xy, ground_height, turpos, gun_power, xlocation, randomHeight, barrierWidth,pTankx,pTanky):
	damage = 0
	currentpower =1
	power_find = False
	while not power_find:
		currentpower +=1
		if currentpower>100:
			power_find =True
		fire = True
		startingshell = list(xy)
		while fire:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
            #pygame.draw.circle(screen, fire_red, (startingshell[0], startingshell[1]), 5)
			startingshell[0] += (12 - turpos) * 2
			startingshell[1] += int((((startingshell[0] - xy[0]) * 0.013 / (currentpower / 50)) ** 2) - (turpos + turpos / (12 - turpos)))
			if startingshell[1] > screen_height - ground_height:
				hit_x = int((startingshell[0] * (screen_height - ground_height / 2)) / startingshell[1])
				hit_y = int(screen_height - ground_height)
				if pTankx+15 > hit_x > pTankx-15:
					power_find= True
				fire = False

			check_x_1 = startingshell[0] <= xlocation + barrierWidth
			check_x_2 = startingshell[0] >= xlocation

			check_y_1 = startingshell[1] >= screen_height - randomHeight
			check_y_2 = startingshell[1] <= screen_height
			if check_x_1 and check_x_2 and check_y_1 and check_y_2:
				hit_x = startingshell[0]
				hit_y = startingshell[1]
				fire = False

	fire = True
	startingshell = list(xy)
	while fire:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		pygame.draw.circle(screen, fire_red, (startingshell[0], startingshell[1]), 5)
		startingshell[0] += (12 - turpos) * 2
		startingshell[1] += int((((startingshell[0] - xy[0]) * 0.013 / (currentpower / 50)) ** 2) - (turpos + turpos / (12 - turpos)))
		if startingshell[1] > screen_height - ground_height:
			hit_x = int((startingshell[0] * (screen_height - ground_height / 2)) / startingshell[1])
			hit_y = int(screen_height - ground_height)
			if pTankx+15 > hit_x > pTankx-15:
				damage= 25
			explosion(hit_x, hit_y)
			fire = False

		check_x_1 = startingshell[0] <= xlocation + barrierWidth
		check_x_2 = startingshell[0] >= xlocation
		check_y_1 = startingshell[1] >= screen_height - randomHeight
		check_y_2 = startingshell[1] <= screen_height
		if check_x_1 and check_x_2 and check_y_1 and check_y_2:
			hit_x = startingshell[0]
			hit_y = startingshell[1]
			explosion(hit_x,hit_y)
			fire = False


		pygame.display.update()
		clock.tick(100)
	return damage



#start menu function
def game_intro():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()	
			if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						quit()	
					elif event.key == pygame.K_c:
						gameloop()	
		screen.fill(white)
		message_to_screen("Welcome to tanks",green,-100, size='medium')
		message_to_screen("The objective of game is to shoot",black,-50, size='small')
		message_to_screen(" and destroy the enemy tank",black,-20, size='small')
		message_to_screen("The more enemy you destryo,",black,10, size='small')
		message_to_screen("the more harder the enemy get",black,40, size='small')
		#message_to_screen("Press C to play, P to pause or Q to quit ",black,100, size='small')

		#putting buttons on screen
		button('play',(screen_width/2)-200,500,100,50, green, light_green,action='p')
		button('controls',(screen_width/2)-50,500,120,50,yellow, light_yellow, action='c')
		button('quit',(screen_width/2)+130,500,100,50, red, light_red,action='q')
		
		pygame.display.update()
		clock.tick(5)

#creating barrier
def barrier(xlocation,randomHeight,barrierWidth):
	
	pygame.draw.rect(screen,black,[xlocation,screen_height-randomHeight,barrierWidth,randomHeight])

#function for fire power
def power(level):
	if level<=0:
		level=0
	elif level>=100:
		level=100
	text = smallfont.render("Power:"+str(level)+"%",True,black)
	screen.blit(text,[screen_width/2,0])


#creating health bars
def health_bar(player_health, enemy_health):
	if player_health >75:
		player_health_color= light_green
	elif player_health >50:
		player_health_color = light_yellow
	else:
		player_health_color = light_red


	if enemy_health >75:
		enemy_health_color= light_green
	elif enemy_health >50:
		enemy_health_color = light_yellow
	else:
		enemy_health_color = red
	pygame.draw.rect(screen,player_health_color,[screen_width-120,25,player_health,25])
	pygame.draw.rect(screen,enemy_health_color,[20,25,enemy_health,25])

#starting the loop for the game:
def gameloop():
	mainTankX= screen_width* 0.9
	mainTankY= screen_height*0.9
	tankMove= 0
	barrierWidth= 50
	enemy_health=100
	player_health=100

	enemyTankX=screen_width*0.1
	enemyTankY= screen_height*0.9

	gameexit = False
	gameover = False
	xlocation = (screen_width/2) + random.randint(-0.2*screen_width, 0.2*screen_width)
	randomHeight = random.randrange(screen_height*0.1, screen_height*0.5)
	currentTurPos= 0
	changeTur = 0
	fire_power = 50
	power_change= 0
	ground_height = screen_height - mainTankY- tankHeight-wheelWidth


	while not gameexit:
		screen.fill(white)
		gun= tank(mainTankX, mainTankY, currentTurPos)
		enemy_gun= enemy_tank(enemyTankX,enemyTankY,8)
		barrier(xlocation, randomHeight, barrierWidth)
		health_bar(player_health,enemy_health)
		screen.fill(green, rect=[0,screen_height-ground_height,screen_width,screen_height])
		power(fire_power)
		#gameover display
		if gameover == True:
			message_to_screen('Game Over',red, -50,size='large')
			message_to_screen(' Press C to play again or Q to quit',green,50,size= 'small') 
			pygame.display.update()

		#this is while loop for replay menu
		while gameover == True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameexit = True
					gameover = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameexit = True
						gameover = False
					elif event.key == pygame.K_c:
						gameloop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameexit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					tankMove= -5
				elif event.key == pygame.K_RIGHT:
					tankMove= +5
				elif event.key == pygame.K_UP:
					changeTur= 1
				elif event.key == pygame.K_DOWN:
					changeTur = -1
				elif event.key == pygame.K_p:
					paused()
				elif event.key == pygame.K_SPACE:
					damage= fireshell(gun,ground_height,currentTurPos,fire_power,xlocation, randomHeight, barrierWidth,enemyTankX,enemyTankY)
					enemy_health -= damage
					damage= e_fireshell(enemy_gun, ground_height, 8, 50, xlocation, randomHeight, barrierWidth,mainTankX,mainTankY)
					player_health -=damage
					#fireshell2(gun, mainTankX, mainTankY, currentTurPos, fire_power)
				elif event.key == pygame.K_a:
					power_change = -1
				elif event.key == pygame.K_d:
					power_change = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					changeTur = 0
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					tankMove = 0
				if event.key == pygame.K_a or event.key == pygame.K_d:
					power_change=0

		mainTankX += tankMove
		fire_power +=power_change

		if mainTankX <xlocation+(tankWidth/2)+barrierWidth:
			mainTankX =xlocation+(tankWidth/2)+barrierWidth
		elif mainTankX > screen_width-(tankWidth/2):
			mainTankX = screen_width-(tankWidth/2)
		if fire_power < 1:
			fire_power= 0
			power_change= 0
		elif fire_power >100:
			power_change=0
			fire_power= 100


#Changing turret position

		currentTurPos += changeTur
		if currentTurPos >8:
			currentTurPos=8
		elif currentTurPos <0:
			currentTurPos =0
		

		#for x in range(25):

		pygame.display.update()
		clock.tick(fps)
	pygame.quit()
	quit()
game_intro()
gameloop()

