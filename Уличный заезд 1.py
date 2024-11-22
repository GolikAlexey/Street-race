import pygame
import random
import os
import sys

from tkinter import *

root=Tk()
root.title("Уличный заезд")
root.geometry("1210x1000")
art_1 = PhotoImage(file = "Меню_Уличный_заезд.Малая версия.png")
edinajaramka=Frame(root, width=1210, height=1000)
edinajaramka.pack(fill=BOTH)

ramkaVerh=Frame(edinajaramka, bd="0", width=1210, height=615)
ramkaVerh.pack(side=TOP, fill=BOTH)

ramkaNiz=Frame(edinajaramka, bd="20", bg="light goldenrod", width=1210, height=385)
ramkaNiz.pack(side=BOTTOM, fill=BOTH)

foto=Label(ramkaVerh, image=art_1, background="light goldenrod")
foto.pack()

knopka1=Button(ramkaNiz, bd=5, text="Выйти  из  игры", font=("arial", 32), background="lime green", activebackground="hot pink", height=1, width=15, command=lambda: root.destroy())
knopka1.pack(side="left", padx="100", pady="100")

knopka2=Button(ramkaNiz, bd=5, text=" ИГРАТЬ ", font=("arial", 32), background="lime green", activebackground="hot pink", height=1, width=15, command=lambda: igra())
knopka2.pack(side="left", padx="100", pady="100")

def igra():
	game_folder = os.path.dirname(__file__)
	img_folder = os.path.join(game_folder, 'Sprajty')
	player_img_1 = pygame.image.load(os.path.join(img_folder, 'Ginka1.jpg'))
	player_img = pygame.transform.scale(player_img_1, (200, 62))
	mob_mashina_img_11 = pygame.image.load(os.path.join(img_folder, 'Ginka_mob_1.jpg'))
	mob_mashina_img_1 = pygame.transform.scale(mob_mashina_img_11, (210, 62))
	mob_mashina_img_22 = pygame.image.load(os.path.join(img_folder, 'Ginka_mob_2.jpg'))
	mob_mashina_img_2 = pygame.transform.scale(mob_mashina_img_22, (210, 62))  
	Karta_Tambark_img_1 = pygame.image.load(os.path.join(img_folder, 'Tambark_1_Ginka_1.jpg'))
	Karta_Tambark_img = pygame.transform.scale(Karta_Tambark_img_1, (8300, 1000))
	
	
    
	SHIRINA = 1900
	VYSOTA = 1000
	FPS = 60
	
	# Задаем цвета
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)
	
	def game_over():
		running = False
		pygame.quit()
		root=Tk()
		root.title("Уличный заезд")
		root.geometry("1200x300")
		root.config(bg="khaki")
		text_game_over=Label(root, text="ВЫ  ПРОИГРАЛИ", font=("Verdana", 90), fg="DarkGreen", background="khaki")
		text_game_over.pack(anchor=CENTER)
		knopka_game_over=Button(root, bd=5, text="OK", font=("arial", 32), background="lime green", activebackground="hot pink", height=1, width=4, command=lambda: root.destroy())
		knopka_game_over.pack(anchor=CENTER)
		
	
	class Mashina1(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image = player_img
			self.rect = self.image.get_rect()
			self.rect.center = (130, 830)
			
		def update(self):
			keys = pygame.key.get_pressed()
			if keys[pygame.K_UP]:
					self.rect.y -=2
			if keys[pygame.K_DOWN]:
					self.rect.y +=2
			if (self.rect.y > 904) or (self.rect.y <715):
				game_over() 
			
			

	class Urovjenj1(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image = Karta_Tambark_img
			self.rect = self.image.get_rect()
			self.rect.bottomright = (8300, 1000)
        
        
		def update(self):
			self.rect.x -= 2
			if self.rect.left < -6400:
				self.rect.right = 8300
				
				
	class Mob1(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image = mob_mashina_img_1
			self.rect = self.image.get_rect()
			self.rect.x = random.randrange(1950, 2100)
			self.rect.y = random.randrange(716, 903)
			self.speedy = random.randrange(10, 15) 
		def update(self):
			self.rect.x -= self.speedy
			if self.rect.left < -250:
				self.rect.x = random.randrange(1950, 2100)
				self.rect.y = random.randrange(716, 903)
				self.speedy = random.randrange(10, 15)
				
	class Mob2(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image = mob_mashina_img_2
			self.rect = self.image.get_rect()
			self.rect.x = random.randrange(2400, 2600)
			self.rect.y = random.randrange(716, 903)
			self.speedy = 9 
		def update(self):
			self.rect.x -= self.speedy
			if self.rect.left < -250:
				self.rect.x = random.randrange(2400, 2600)
				self.rect.y = random.randrange(716, 903)
				self.speedy = 9


	# Создаем игру и окно
	pygame.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((SHIRINA, VYSOTA))
	pygame.display.set_caption("Уличный заезд")
	clock = pygame.time.Clock()
	vsje_sprajty = pygame.sprite.Group()
	karta_1 = Urovjenj1()
	vsje_sprajty.add(karta_1)
	player = Mashina1()
	vsje_sprajty.add(player)
	mobs = pygame.sprite.Group()
	mob1 = Mob1()
	vsje_sprajty.add(mob1)
	mobs.add(mob1)
	mob2 = Mob2()
	vsje_sprajty.add(mob2)
	mobs.add(mob2)
	


	# Цикл игры
	running = True
	while running:
		# Держим цикл на правильной скорости
		clock.tick(FPS)
		# Ввод процесса (события)
		for event in pygame.event.get():
			# check for closing window
			if event.type == pygame.QUIT:
				running = False
			
			
		# Обновление
		vsje_sprajty.update()
		stolknovjenije = pygame.sprite.spritecollide(player, mobs, False)
		if stolknovjenije:
			game_over()
		
    
		# Рендеринг
		screen.fill(WHITE)
		vsje_sprajty.draw(screen)
		
		# После отрисовки всего, переворачиваем экран
		pygame.display.flip()

	pygame.quit()


	
	

root.mainloop() 
