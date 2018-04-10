import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,panel,x,midY,top):
        pygame.sprite.Sprite.__init__(self)
        self.screen = panel
        self.x = x
        self.midY = midY
        self.top = top
        self.image = pygame.image.load("obs.png")
        self.rect = self.image.get_rect()
        self.w = self.rect.width
        
        
        self.paint()

    def updateDisplay(self):
        self.screen.blit(self.image,(self.x,self.y))
        self.rect.x,self.rect.y = self.x,self.y
        
    
