from layer_naive import *

apple = 100
apple_num = 2
tax = 1.1

#layer
mul_apple_layer = MulLayer()
mul_tax_Layer = MulLayer()

#forward
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_Layer.forward(apple_price, tax)

#backward
dprice = 1
dapple_price, dtax = mul_tax_Layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print("値段 :",int(price))
print(dapple, int(dapple_num), dtax)

