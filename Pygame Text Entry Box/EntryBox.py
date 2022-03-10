import pygame

addChar = lambda string, char, pos : string[:pos] + char + string[pos:]

removeChar = lambda string, pos : string[:pos] + string[pos+1:]

typable = """ !"#$%&\\ '()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

class EntryBox():
	def __init__(self, rect, textSize):
		self.rect = rect
		self.textSize = textSize
		self.color = "gray"
		self.borderColor = "white"
		self.borderWidth = 5

		self.selected = 0
		self.texts = [""]
		self.cursorPos = [0, 0]

		self.font = pygame.font.SysFont('Arial', self.textSize)

	def draw(self, win):
		pygame.draw.rect(win, self.color, self.rect)
		pygame.draw.rect(win, self.borderColor, self.rect, width = self.borderWidth)

		for i, text in enumerate(self.texts):
			surfaceText = self.font.render(self.texts[i], 1, (0, 0, 0), self.color)
			win.blit(surfaceText, (self.rect.x + self.borderWidth, self.rect.y + self.borderWidth + i * self.textSize))

		return(win)

	def updateEvent(self, events):
		for event in events:
			match event.type:
				case pygame.MOUSEBUTTONDOWN:
					if(event.button == 1):
						self.selected = self.rect.collidepoint(event.pos)
				case pygame.KEYDOWN:
					if(self.selected):
						code = event.unicode
						match code:
							case "\r":
								self.cursorPos[1] += 1
								if(self.cursorPos[1] >= len(self.texts)):
									self.texts.append("")
									self.cursorPos[0] = 0
							case "\x08":
								if(self.cursorPos[0] != 0):
									self.texts[self.cursorPos[1]] = removeChar(self.texts[self.cursorPos[1]], self.cursorPos[0]-1)
									self.cursorPos[0] -= 1
								else:
									if(self.cursorPos[1] != 0):
										self.cursorPos[1] -= 1
										self.cursorPos[0] = len(self.texts[self.cursorPos[1]])
										self.texts = self.texts[:-1]
							case _:
								if(code != ""):
									self.texts[self.cursorPos[1]] = addChar(self.texts[self.cursorPos[1]], code, self.cursorPos[0])
									self.cursorPos[0] += 1
