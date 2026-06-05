import pygame

class Snake: 
    def __init__(self):
        self.pos_x = 300
        self.pos_y = 300
        self.dir_x = 0
        self.dir_y = 0
        self.size = 20
        self.alive = True  
        self.body = [(self.pos_x, self.pos_y)]  # Le corps du serpent 
        self.length = 1  # Longueur du serpent 

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.dir_y == 0:
                self.dir_x = 0
                self.dir_y = -1
            elif event.key == pygame.K_DOWN and self.dir_y == 0:
                self.dir_x = 0
                self.dir_y = 1
            elif event.key == pygame.K_LEFT and self.dir_x == 0:
                self.dir_x = -1
                self.dir_y = 0
            elif event.key == pygame.K_RIGHT and self.dir_x == 0:
                self.dir_x = 1
                self.dir_y = 0
        if self.alive:
            self.pos_x += self.dir_x * self.size
            self.pos_y += self.dir_y * self.size
             # Ajouter la nouvelle tête
        new_head = (self.pos_x, self.pos_y)
        self.body.insert(0, new_head)  #

        # Si la longueur du serpent est plus grande, on retire le dernier segment
        if len(self.body) > self.length:
            self.body.pop()  # Supprimer queue (derniere case)
        
        # verif si tete touche corps
        if (new_head) in self.body[1:]:
            self.alive = False  # Si oui serpent meurt
    
      

            