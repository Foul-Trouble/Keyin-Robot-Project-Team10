import robot_mac
import matplotlib as plt
r = robot_mac.RobotController()
r.connect()
room_1_temp = 0
room_2_temp = 0
room_3_temp = 0
room_4_temp = 0
room_5_temp = 0


def plot_temp():
    xs = ["Room 1", "Room 2", "Room 3", "Room 4", "Room 5", "Hall"]
    ys = [room_1_temp, room_2_temp, room_3_temp, room_4_temp, room_5_temp, hall_temp]
    plt.plot(xs, ys)
    plt.show()


def fire_loop():
    Fire = True
    while Fire:
        if r.scan_for_fire():
            r.extinguish_fire()
        else:
            Fire = False


def hallway(location):
    global room_1_temp
    global room_2_temp
    global room_3_temp
    global room_4_temp
    global room_5_temp
    if location == 1:
        r.forward(390)
        r.left(130)
        if r.read_marker() == 3:
            #   Go into room 1
            print("Going into room 1!")
            r.left(690)
            if r.scan_for_people:
                r.rescue_person()
                room_1_temp = r.take_temperature()
                r.right(820)
                r.backward(390)
            else:
                room_1_temp = r.take_temperature()
                r.right(820)
                r.backward(390)
        else:
            #   Go on to room 2
            r.right(130)
            r.forward(550)
            r.left(130)
            if r.read_marker() == 3:
                #   Go into room 2
                print("Going into room 2!")
                r.left(600)
                r.forward(75)
                fire_loop()
            else:
                r.right(130)
                r.forward(510)
                r.left(1850)


    if location == 2:
        r.forward(950)
        r.left(200)
        mark = r.read_marker()
        print(mark)
        if mark == 1:
            r.left(600)
            r.forward(150)
            global room_2_temp
            room_2_temp = r.take_temperature()
            fire_loop()
            r.backward(150)
            r.right(600)
        else:
            r.right(200)
            r.forward(500)
            r.left
            


hallway(1)