#Yavuz Selim Suzen, 101215831

import pygame

#Loading an image
img = pygame.image.load('alex.png')

#Getting size of the image
(w,h) = img.get_size()

#Creating window and its weight and height is same with the image's size
window = pygame.display.set_mode((w , h))

#Blitting
window.blit(img, (0,0))

#Creating a funcyion, it makes photomanipulation 
def board(window, w, h, mx, my):
	for my in range(my-5, my+6):
		for mx in range(w):
		
			
													 
			(r,g,b,_) = window.get_at((mx , my))
													
			window.set_at((mx,my) , (255-r, 255-g, 255-b))
	
			
		
	



#Creating an infinite loop
while True:
	#If user click the close, the loop will end
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()	
		#If user uses mouse, he/she only can use left click		
		if event.type == pygame.MOUSEBUTTONDOWN:
			key = pygame.mouse.get_pressed()
			#left click 
			if (key[0]):
				#Getting x,y coordinate
				(mx,my) = pygame.mouse.get_pos()
				#Using the function
				board(window,w,h,mx,my)
				#Display update
				pygame.display.update()		
								
					
							
						
