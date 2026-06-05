import os
os.chdir(os.path.dirname(__file__))
import pygame, sys
from snake import Snake
from apple import Apple




class Game:


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.start_screen = True
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0
        self.score_list = [0, 0] 
        self.running = True
    

    def UI(self, font_name, size, text, position, color):
        font = pygame.font.SysFont(font_name, size)
        text_surface = font.render(text, True, color)  # True = antialiasing
        text_rect = text_surface.get_rect()
        text_rect.center = position  # Placer le texte à la position donnée (x, y)
        self.screen.blit(text_surface, text_rect)
    

    def run_game(self):
        
        while self.start_screen :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RETURN :
                        self.start_screen = False
                self.screen.fill((255, 255, 255))
                self.UI("Arial", 30, "Appuyez sur Entrée pour jouer", (400, 300), (255, 0, 0)) 
                pygame.display.flip()
            


        while self.running == True :
            self.clock.tick(10)  # 10 frames/sec = vitesse du snake
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Paramètre de l'écran
            self.screen.fill((0, 0, 0))
            border_thickness = 20
            screen_width, screen_height = self.screen.get_size()

            # Vérification de la collision avec le mur avant de déplacer le serpent
            if (self.snake.pos_x <= 20 or self.snake.pos_x + self.snake.size >= 800 - 20 or
                self.snake.pos_y <= 20 or self.snake.pos_y + self.snake.size >= 600 - 20):
                print(" Collision avec le mur ! Reset...")
                if self.score > self.score_list[0] :
                    self.score_list.insert(0, self.score)
                else : 
                    self.score_list.insert(1, self.score)
                self.score = 0
                self.snake = Snake()  # Réinitialiser le serpent à sa position et taille initiale

            # Vérification si le serpent se mord
            if not self.snake.alive: # snake.alive = variable qui permet au serpent de bouger dans snake et detecte la morsure dans snake
                if self.score > self.score_list[0] :
                    self.score_list.insert(0, self.score)
                else : 
                    self.score_list.insert(1, self.score) 
                print(" serpent mordu!")
                self.score = 0
                self.snake = Snake()  # Réinitialiser le serpent pour recommencer le jeu
                self.apple = Apple()
                                   

            self.snake.move(event)  # Déplacer le serpent après les vérifications

            self.UI("Arial", 20, f"Score : {self.score}", (80, 40), (255, 0, 0))
            self.UI("Arial", 20, f"Meilleur score : {self.score_list[0]}", (100, 60), (255, 0, 0))
            

            # Créer des objets Rect pour le serpent et la pomme
            snake_rect = pygame.Rect(self.snake.pos_x, self.snake.pos_y, self.snake.size, self.snake.size)
            apple_rect = pygame.Rect(self.apple.pos_x, self.apple.pos_y, self.apple.size, self.apple.size)


            # Vérifier la collision entre le serpent et la pomme
            if snake_rect.colliderect(apple_rect):  # Si le serpent touche la pomme
                print(" Collision avec la pomme !")
                self.apple = Apple()  # Créer une nouvelle pomme
                self.snake.length += 1  # Faire grandir le serpent
                self.score += 1



            # Dessiner les éléments
            pygame.draw.rect(self.screen, (255, 0, 255), (0, 0, screen_width, screen_height), border_thickness)  # Bordure
            
            for i, segment in enumerate(self.snake.body):  # Dessiner chaque segment du corps du serpent
                # Si c'est le dernier segment (la queue)
                if i == 0:  # Si c'est le premier segment (la tete)
                        pygame.draw.rect(self.screen, (0, 0, 255), (segment[0], segment[1], self.snake.size, self.snake.size))  # Tête en vert
                elif i == len(self.snake.body) - 1:  # Si c'est le dernier segment (la queue)
                        pygame.draw.rect(self.screen, (255, 0, 0), (segment[0], segment[1], self.snake.size, self.snake.size))  # Queue en rouge
                else:  # Si c'est un segment intermédiaire du corps
                        pygame.draw.rect(self.screen, (0, 255, 0), (segment[0], segment[1], self.snake.size, self.snake.size))  # Serpent en vert

            pygame.draw.rect(self.screen, (255, 0, 0), (self.apple.pos_x, self.apple.pos_y, self.apple.size, self.apple.size))  # Pomme



            pygame.display.flip()




if __name__ == "__main__":
    Game().run_game()