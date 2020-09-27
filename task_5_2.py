symbol = '*'

row_for_up = 1
for one_symbol in range(5):
    print(symbol * row_for_up)
    row_for_up += 1

row_for_down = 4
for one_symbol in range(4):
    print(symbol * row_for_down)
    row_for_down -= 1