from mcpi.minecraft import Minecraft
mc = Minecraft.create()

buildX = -72
buildY = 10
buildZ = 51
width = 10
height = 5
length = 6

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = (buildX < x < buildX + width) and (buildY <= y <= buildY + height) and (buildZ <= z <= buildZ + length)
mc.postToChat("The player is in their house: " + str(inside))
print("vocaloid.wikia.com")


#-69, 10, 51
