#inventory.py
'''
displays a players inventory and the amount
of items per type.abs
'''

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v;
    print("\nTotal number of items: " + str(item_total))


'''
write a function that adds loot on to the players inventory
'''
def addToInventory(inventory,addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] +=1
        else:
            inventory[item] = 1

def main():
    dragonLoot = ['gold coin', 'dagger','gold coin','gold coin', 'ruby']
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    addToInventory(stuff,dragonLoot)
    displayInventory(stuff)

main()
