import pygame, sys
from EntryBox import EntryBox

def checkEvent(events):
	global winOpen
	for event in events:
		match event.type:
			case pygame.QUIT:
				winOpen = 0

pygame.init()

win = pygame.display.set_mode((400, 400), pygame.RESIZABLE, pygame.DOUBLEBUF)

entry = EntryBox(pygame.Rect(50, 50, 100, 50), 15)

winOpen = 1
while(winOpen):
	win.fill(0)

	events = pygame.event.get()
	
	checkEvent(events)
	entry.updateEvent(events)
	win = entry.draw(win)
	print(entry.texts, entry.cursorPos)

	pygame.display.update()

pygame.quit()
sys.exit()