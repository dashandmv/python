colors = {'red':'красный', 'green':'зеленый', 'blue':'синий', 'purpule':'голубой'}

colors.update({'yellow':'желтый'})
print(colors)

del colors['red']
print(colors)

k = list(colors.keys())
print(k)

v = list(colors.values())
print(v)

colors.clear()
print(colors)
