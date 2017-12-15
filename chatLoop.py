from mcpi.minecraft import Minecraft
mc = Minecraft.create()
username = input("please enter username:")

while True:
    message = input("Enter Your message")
    if message == "exit" :
        break
    else:
        mc.postToChat(username + ":" + message)
