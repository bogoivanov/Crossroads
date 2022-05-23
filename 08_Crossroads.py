from collections import deque

green_window = int(input())
free_window = int(input())

cars = deque()
passed_cars = 0
has_crashed = False

while True:
    line = input()
    if line == "END":
        break

    if line == "green":
        current_green = green_window
        while cars and current_green > 0:
            car = cars.popleft()
            if current_green >= len(car) or current_green + free_window >= len(car):
                passed_cars += 1
                current_green -= len(car)
            else:
                print(f"A crash happened!")
                print(f"{car} was hit at {car[current_green + free_window]}.")
                has_crashed = True
                break
    else:
        cars.append(line)

if not has_crashed:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")




# from collections import deque
#
# green_light_duration = int(input())
# free_window_duration = int(input())
# passed_cars = 0
# cars_deque = deque()
# crash = False
# while True:
#     command = input()
#     if command == "END":
#         break
#     elif command == "green":
#         green_light = green_light_duration
#         free_window = free_window_duration
#         if cars_deque:
#             while cars_deque and green_light > 0:
#                 car = cars_deque[0]
#                 if green_light >= len(car):
#                     cars_deque.popleft()
#                     passed_cars += 1
#                     green_light -= len(car)
#
#                 elif green_light + free_window >= len(car):
#                     cars_deque.popleft()
#                     passed_cars += 1
#                     green_light = 0
#                     free_window -= abs(green_light - len(car))
#
#                 else:
#                     index = green_light + free_window
#                     print(f"A crash happened!")
#                     print(f"{cars_deque[0]} was hit at {cars_deque[0][index]}.")
#                     crash = True
#                     break
#         else:
#             break
#     else:
#         cars_deque.append(command)
#
# if not crash:
#     print("Everyone is safe.")
#     print(f"{passed_cars} total cars passed the crossroads.")
#
#

