import pyautogui
import keyboard

def move_up():
	pyautogui.moveRel(0,-20)
def move_down():
	pyautogui.moveRel(0,20)
def move_left():
	pyautogui.moveRel(-20,0)
def move_right():
	pyautogui.moveRel(20,0)
# Diagonals	
def diagonal_up_left():
	pyautogui.moveRel(-20,-20)
def diagonal_up_right():
	pyautogui.moveRel(20,-20)
def diagonal_down_left():
	pyautogui.moveRel(-20,20)
def diagonal_down_right():
	pyautogui.moveRel(20,20)
# left and right click
def click_left():	
	pyautogui.mouseDown(button='left')		
def click_right():	
	pyautogui.click(button='right')
def click_middle():
	pyautogui.click(button='middle')
# Scroll
def scroll_up():
	pyautogui.scroll(-100)
def scroll_down():
	pyautogui.scroll(100)

# Key block preventing writing while pressing keys
keyboard.block_key(72) # block numpad 8
keyboard.block_key(82) # block numpad 0
keyboard.block_key(83) # block numpad .
keyboard.block_key(79) # block numpad 1
keyboard.block_key(80) # block numpad 2
keyboard.block_key(81) # block numpad 3
keyboard.block_key(75) # block numpad 4
keyboard.block_key(76) # block numpad 5
keyboard.block_key(77) # block numpad 6
keyboard.block_key(71) # block numpad 7

keyboard.block_key(73) # block numpad 9
keyboard.block_key(78) # block numpad +
keyboard.block_key(74) # block numpad -
on = True
while(True):
	while(on == True):				
		###################################		
		if(keyboard.is_pressed(72)):
			move_up()		
		if(keyboard.is_pressed(80)):
			move_down()			
		if(keyboard.is_pressed(75)):
			move_left()			
		if(keyboard.is_pressed(77)):
			move_right()			
			
		# diagonal
		if(keyboard.is_pressed(71)):
			diagonal_up_left()		
		if(keyboard.is_pressed(73)):
			diagonal_up_right()		
		if(keyboard.is_pressed(79)):
			diagonal_down_left()		
		if(keyboard.is_pressed(81)):
			diagonal_down_right()
		
		#  left, right and middle click
		
		if(keyboard.is_pressed(82)):
			click_left()
			if (keyboard.is_pressed(82) == False):
				pyautogui.mouseUp(button='left')
		if(keyboard.is_pressed(83)):			
			click_right()
		if(keyboard.is_pressed(76)):
			click_middle()
		#Scroll up and down
		
		if(keyboard.is_pressed(78)):
			scroll_up()		
		if(keyboard.is_pressed(74)):		
			scroll_down()			
			
		################################ Leave
		if(keyboard.is_pressed("q")):
			print("pause")
			on = False
	if(keyboard.is_pressed("w")):
			print("resume")
			on = True

print("enter a key")