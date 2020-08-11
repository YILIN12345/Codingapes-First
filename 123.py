
from mcpi.minecraft import Minecraft
import random
mc=Minecraft.creat()
x,y,z = mc.player.getTilePos()

wallet_a = random.randrange(0,10)
wallet_b = random.randrange(0,10)

if wallet_a == 4 or wallet_a == 8:
    print("4or8")
    
total = wallet_a + wallet_b

if total>10:
    print("yes")
    
print(wallet_a)
print(wallet_b)

try:
    blockType = int(input("Block id:"))
    print("valid")
except:
    print("Inval id")