

ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2: #raise Exception("Products in cart count not matching")
    pass

assert(ItemsInCart == 0)

#try , catch

try:
    with open('../venv/test.txt', 'r') as reader:
        reader.read()

except:
    print("Failure in try block")

try:
    with open('../venv/test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up resources")