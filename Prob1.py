from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
	max_value = max(data) if data else 0
	histogram = [0] * (max_value + 1)
	
	for num in data:
		histogram[num] += 1
    
	return histogram
    

#1b
def print_histogram(hist: list[int]) -> None:
    for index, count in enumerate(hist):
        print(f"{index}: {'*' * count}")


#1c
def graph_histogram(hist: list[int], width: int, height: int) -> None:
    gw = GWindow(width, height)
    
    max_count = max(hist) if hist else 1  

    bar_width = width / len(hist)
    
    for i, count in enumerate(hist):
        bar_height = (count / max_count) * (height - 20) 

        x = i * bar_width
        y = height - bar_height
        
        bar = GRect(bar_width - 2, bar_height)  
        bar.set_filled(True)
        bar.set_color("red")
        
        gw.add(bar, x, y)
    
    gw.mainloop()


# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
#print_histogram(hist) # uncomment to test
#graph_histogram(hist, 400, 400) # uncomment to test

print_histogram(hist)
graph_histogram(hist, 400, 400)
