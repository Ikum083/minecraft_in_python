# instead of importing everything from the ursina engine we use import ursina as urs to avoid problems
import ursina as urs
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()
# create main class
class MainGame:
  # create construct to initialize variables
  def __init__(self):
    self.boxes = []
    for i in range(20):
      for j in range(20):
        self.box = urs.Button(color=color.white, model='cube', position=(j,0,i),
              texture='grass.png', parent=scene, origin_y=0.5)
        self.boxes.append(box)

def input(key):
  for box in boxes:
    if box.hovered:
      if key == 'left mouse down':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == 'right mouse down':
        boxes.remove(box)
        destroy(box)

app.run()