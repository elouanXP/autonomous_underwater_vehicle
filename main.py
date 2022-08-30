import math
import pygame
from auv import Graphics,Auv,Ultrasonic

MAP_DIMENSIONS = (600,1200)

gfx = Graphics(MAP_DIMENSIONS,'auv.png','map_f.png')

start = (200,300)
auv = Auv(start,0.01*3779.52)

sensor_range = 500,math.radians(40)
ultra_sonic = Ultrasonic(sensor_range,gfx.map)

dt = 0
last_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    dt = (pygame.time.get_ticks()-last_time)/1000
    last_time = pygame.time.get_ticks()
    gfx.map.blit(gfx.map_img,(0,0))
    auv.kinematics(dt)
    gfx.draw_auv(auv.x,auv.y,auv.heading)
    point_cloud = ultra_sonic.sense_obstacles(auv.x,auv.y,auv.heading)
    auv.avoid_obstacles(point_cloud,dt)
    gfx.draw_sensor_data(point_cloud)
    
    pygame.display.update()

