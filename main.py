import pygame
import sys
# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
PINK = (255, 105, 180)  # Pembe rengi (RGB)
BLUE = (0, 0, 255)
ORANGE =  (255, 165, 0)
RED =  (255, 0 , 0)
BROWN =  (165, 42, 42)
# Pygame'i başlat
pygame.init()

# Ekran boyutları
screen_width, screen_height = 1200, 900
screen = pygame.display.set_mode((screen_width, screen_height))


# Başlık
background_image = pygame.image.load("dilovasi.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Yazı tipi ayarları
font_size = 30
font = pygame.font.Font(None, font_size)
text_1 = "Hospital"
text_surface_1 = font.render(text_1, True, (0, 0, 0))  
text_rect_1 = text_surface_1.get_rect(bottomleft=(70, screen_height - 65))  # Sol alt köşeye yerleştir

text_2 = "School"
text_surface_2 = font.render(text_2, True, (0, 0, 0))  
text_rect_2 = text_surface_2.get_rect(bottomleft=(70, screen_height - 125))  # Sol alt köşeye yerleştir

text_3 = "Population"
text_surface_3 = font.render(text_3, True, (0, 0, 0))  
text_rect_3 = text_surface_3.get_rect(bottomleft=(70, screen_height - 185))  # Sol alt köşeye yerleştir

text_4 = "Park"
text_surface_4 = font.render(text_4, True, (0, 0, 0))  
text_rect_4 = text_surface_4.get_rect(bottomleft=(70, screen_height - 245))  # Sol alt köşeye yerleştir

text_5 = "Factory Areas"
text_surface_9 = font.render(text_5, True, (0, 0, 0))  
text_rect_9 = text_surface_9.get_rect(bottomleft=(70, screen_height - 305))  # Sol alt köşeye yerleştir



text_population_1 = "12834"
text_surface_5 = font.render(text_population_1, True, BLACK)  
text_rect_5 = text_surface_5.get_rect(center=(screen_width // 2, screen_height //2))  # Sol alt köşeye yerleştir

text_population_2 = "12329"
text_surface_6 = font.render(text_population_2, True, BLACK)  
text_rect_6 = text_surface_6.get_rect(center=(screen_width // 2 - 200 , screen_height // 2 - 200 ))  # Sol alt köşeye yerleştir

text_population_3 = "2638"
text_surface_7 = font.render(text_population_3, True, BLACK)  
text_rect_7 = text_surface_7.get_rect(center=(screen_width // 2  - 100 , screen_height // 2 + 220))  # Sol alt köşeye yerleştir

text_population_4 = "2716"
text_surface_8 = font.render(text_population_4, True, BLACK)  
text_rect_8 = text_surface_8.get_rect(center=(screen_width // 2 + 400 , screen_height // 2 +50))  # Sol alt köşeye yerleştir


text_population_10 = "2716"
text_surface_10 = font.render(text_population_10, True, BLACK)  
text_rect_10 = text_surface_10.get_rect(center=(screen_width // 2  , screen_height // 2 ))  # Sol alt köşeye yerleştir



pygame.display.set_caption('GreenZone Interactive Community Map')



# Form kutusunun boyutları
box_width, box_height = 35, 35
box_x, box_y_1 = 25, (screen_height - box_height) - 60  # İlk kutunun y koordinatı
box_y_2 = (screen_height - box_height) - 120  # İkinci kutunun y koordinatı
box_y_3 = (screen_height - box_height) - 180
box_y_4 = (screen_height - box_height) - 240
box_y_5 = (screen_height - box_height) - 300
box_rect_1 = pygame.Rect(box_x, box_y_1, box_width, box_height) 
box_rect_2 = pygame.Rect(box_x, box_y_2, box_width, box_height)
box_rect_3 = pygame.Rect(box_x, box_y_3, box_width, box_height)
box_rect_4 = pygame.Rect(box_x, box_y_4, box_width, box_height)
box_rect_5 = pygame.Rect(box_x, box_y_5, box_width, box_height)



# Tik kutusu aktif/pasif durumu (başlangıçta pasif)
ticked_1 = False
ticked_2 = False
ticked_3 = False
ticked_4 = False
ticked_5 = False

# Ana döngü
running = True
while running:
 
    # Etkinlikleri kontrol et
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        # Mouse tıklama olayı
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Eğer form kutusuna tıklandıysa
            if box_rect_1.collidepoint(event.pos):


                ticked_1 = not ticked_1  # İlk kutunun durumunu değiştir
                
                
            elif box_rect_2.collidepoint(event.pos):
                ticked_2 = not ticked_2  # İkinci kutunun durumunu değiştir
            elif box_rect_3.collidepoint(event.pos):
                ticked_3 = not ticked_3  # İlk kutunun durumunu değiştir
            elif box_rect_4.collidepoint(event.pos):
                ticked_4 = not ticked_4  # İkinci kutunun durumunu değiştir
            elif box_rect_5.collidepoint(event.pos):
                ticked_5 = not ticked_5  # İkinci kutunun durumunu değiştir

    # Arka planı ekrana çiz
    screen.blit(background_image, (0, 0))

    # Form kutularını çiz
    pygame.draw.rect(screen, BROWN, box_rect_1)
    pygame.draw.rect(screen, BLUE, box_rect_2)
    pygame.draw.rect(screen, ORANGE, box_rect_3)
    pygame.draw.rect(screen, GREEN, box_rect_4)
    pygame.draw.rect(screen, RED, box_rect_5)

    # Eğer ilk tik aktifse kutuya tik işareti koy
    if ticked_1:
        pygame.draw.line(screen, BLACK, (box_x + 10, box_y_1 + 10), (box_x + box_width - 10, box_y_1 + box_height - 10), 5)
        pygame.draw.line(screen, BLACK, (box_x + box_width - 10, box_y_1 + 10), (box_x + 10, box_y_1 + box_height - 10), 5)
        pygame.draw.circle(screen, BROWN, (screen_width - 135, screen_height // 2 - 15), 15)
    # Eğer ikinci tik aktifse kutuya tik işareti koy
    if ticked_2:
        pygame.draw.line(screen, BLACK, (box_x + 10, box_y_2 + 10), (box_x + box_width - 10, box_y_2 + box_height - 10), 5)
        pygame.draw.line(screen, BLACK, (box_x + box_width - 10, box_y_2 + 10), (box_x + 10, box_y_2 + box_height - 10), 5)
        pygame.draw.circle(screen, BLUE, (screen_width // 2 - 200, screen_height // 2 -30 ), 15)
        pygame.draw.circle(screen, BLUE, (screen_width // 2  + 135, screen_height // 2 +70 ), 15)
    if ticked_3:
        pygame.draw.line(screen, BLACK, (box_x + 10, box_y_3 + 10), (box_x + box_width - 10, box_y_3 + box_height - 10), 5)
        pygame.draw.line(screen, BLACK, (box_x + box_width - 10, box_y_3 + 10), (box_x + 10, box_y_3 + box_height - 10), 5)
        pygame.draw.circle(screen, ORANGE,(screen_width // 2  , screen_height // 2  ), 100) 
        pygame.draw.circle(screen, ORANGE, (screen_width // 2 - 200 , screen_height // 2 - 200  ), 86)
        pygame.draw.circle(screen, ORANGE, (screen_width // 2  - 100 , screen_height // 2 + 220  ), 20)
        pygame.draw.circle(screen, ORANGE, (screen_width // 2 + 400 , screen_height // 2 +50  ), 20)
        screen.blit(text_surface_5, text_rect_5)
        screen.blit(text_surface_6, text_rect_6)
        screen.blit(text_surface_7, text_rect_7)
        screen.blit(text_surface_8, text_rect_8)

    if ticked_4:
        pygame.draw.line(screen, BLACK, (box_x + 10, box_y_4 + 10), (box_x + box_width - 10, box_y_4 + box_height - 10), 5)
        pygame.draw.line(screen, BLACK, (box_x + box_width - 10, box_y_4 + 10), (box_x + 10, box_y_4 + box_height - 10), 5)
        pygame.draw.circle(screen, GREEN, (screen_width // 2 - 270 , screen_height // 2   ), 20) 
        pygame.draw.circle(screen, GREEN, (screen_width // 2 - 100 , screen_height // 2  + 150 ), 20)
        pygame.draw.circle(screen, GREEN, (screen_width // 2  , screen_height // 2  +320 ), 20)
        pygame.draw.circle(screen, GREEN, (screen_width // 2 + 300 , screen_height // 2  +15 ), 20)
        pygame.draw.circle(screen, GREEN, (screen_width // 2 + 270 , screen_height // 2 - 300  ), 20)
        pygame.draw.circle(screen, GREEN, (screen_width // 2  - 45  , screen_height // 2 - 250  ), 20)
   
    if ticked_5:
        pygame.draw.line(screen, BLACK, (box_x + 10, box_y_5 + 10), (box_x + box_width - 10, box_y_5 + box_height - 10), 5)
        pygame.draw.line(screen, BLACK, (box_x + box_width - 10, box_y_5 + 10), (box_x + 10, box_y_5 + box_height - 10), 5)
        pygame.draw.circle(screen, RED, (screen_width // 2 - 330 , screen_height // 2  +100  ), 20)
        pygame.draw.circle(screen, RED, (screen_width // 2 - 500 , screen_height // 2  + 120  ), 20)
        pygame.draw.circle(screen, RED, (screen_width // 2 - 400 , screen_height // 2  +60  ), 20)
        pygame.draw.circle(screen, RED, (screen_width // 2 - 140 , screen_height // 2  + 400  ), 20)
        pygame.draw.circle(screen, RED, (screen_width // 2 - 200 , screen_height // 2  + 330  ), 20)
        pygame.draw.circle(screen, RED, (screen_width // 2  - 100 , screen_height // 2  - 360  ), 20)
        pygame.draw.circle(screen, RED,  (screen_width // 2  + 40 , screen_height // 2  + 430  ), 20)


   

    
    # Ekranı güncelle
    screen.blit(text_surface_1, text_rect_1)
    screen.blit(text_surface_2, text_rect_2)
    screen.blit(text_surface_3, text_rect_3)
    screen.blit(text_surface_4, text_rect_4)
    screen.blit(text_surface_9, text_rect_9)
    
    pygame.display.flip()

# Pygame'den çık
pygame.quit()
sys.exit()
