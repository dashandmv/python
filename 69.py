weather = {'moscow':20, 'kazan':30, 'anapa':35}
counter = 0
counter_2 = 0
for i in list(weather.keys()):
    counter += weather[i]
    counter_2 += 1
print(counter/counter_2)
    
    
