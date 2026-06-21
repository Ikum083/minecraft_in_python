# instead of importing everything from the ursina engine we use import ursina as urs to avoid problems
import ursina as urs
from ursina.prefabs.first_person_controller import FirstPersonController

# create main class
# inherit 
class MainGame(urs.Entity):
  # create construct to initialize variables
  def __init__(self):
    super().__init__(self)
    self.__boxes = []
    for i in range(20):
      for j in range(20):
        # minor adjustments for the change in importing the module
        self.__box = urs.Button(color=urs.color.white, model='cube', position=(j,0,i),
              texture='grass.png', parent=urs.scene, origin_y=0.5)
        self.__boxes.append(self.__box)

  # method for player control
  def input(self,key):
    for box in self.__boxes:
      if box.hovered:
        if key == 'left mouse down':
          # minor adjustments for the change in importing the module
          new = urs.Button(color=urs.color.white, model='cube', position=box.position + urs.mouse.normal,
                      texture='grass.png', parent=urs.scene, origin_y=0.5)
          self.__boxes.append(new)
        if key == 'right mouse down':
          self.__boxes.remove(box)
          urs.destroy(box)

if __name__ == "__main__":
  app = urs.Ursina()
  main = MainGame()
  player = FirstPersonController()
  urs.Sky()
  app.run()