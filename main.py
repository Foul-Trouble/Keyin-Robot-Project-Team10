import robot_mac
import matplotlib as plt
r = robot_mac.RobotController()
r.connect()
room_1_temp = 0
room_2_temp = 0
room_3_temp = 0
room_4_temp = 0
room_5_temp = 0
hall_temp = 0


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


def hallway():
    global room_1_temp
    global room_2_temp
    global room_3_temp
    global room_4_temp
    global room_5_temp
    global hall_temp

    r.forward(390)
    r.left(130)
    if r.read_marker() == 1:
        #   Go into room 1
        print("Going into room 1!")
        r.left(690)
        if r.scan_for_people:
            print("Rescuing person!")
            r.rescue_person()
            print("Taking room 1 temperature!")
            room_1_temp = r.take_temperature()
            r.right(820)
            r.backward(390)
        else:
            print("Taking room 1 temperature!")
            room_1_temp = r.take_temperature()
            r.right(820)
            r.backward(390)
        r.forward(390)

    else:
        print("Skipping room 1!")
        r.right(130)
    r.forward(550)
    r.left(130)
    if r.read_marker() == 1:
        print("Going into room 2!")
        r.left(600)
        r.forward(75)
        fire_loop()
        print("Taking room 2 temperature!")
        room_2_temp = r.take_temperature()
        r.backward(75)
        r.right(730)
    else:
        print("Skipping room 2!")
        r.right(130)
    r.forward(510)
    r.left(1700)
    r.backward(100)
    r.rotate_counterclockwise(90)
    if r.read_marker() == 2:
        print("Going into room 3!")
        r.rotate_clockwise(90)
        r.backward(200)
        print("Taking room 3 temperature!")
        room_3_temp = r.take_temperature()
        r.forward(300)
    else:
        print("Skipping room 3!")
        r.rotate_clockwise(90)
        r.forward(100)
    r.left(700)
    r.backward(950)
    print("Taking hall temperature!")
    hall_temp = r.take_temperature()
    r.right(800)
    r.backward(820)
    r.rotate_clockwise(90)
    if r.read_marker() == 1:
        print("Going into room 4!")
        r.rotate_counterclockwise(90)
        r.backward(400)
        r.right(700)
        fire_loop()
        print("Taking room 4 temperature!")
        room_4_temp = r.take_temperature()
        r.left(700)
        r.forward(500)
    else:
        print("Skipping room 4!")
        r.rotate_counterclockwise(90)
        r.forward(100)
    r.right(1200)
    r.backward(225)
    r.right(325)
    r.rotate_clockwise(90)
    if r.read_marker() == 1:
        print("Going into room 5!")
        r.rotate_counterclockwise(90)
        r.backward(350)
        r.right(350)
        if r.scan_for_people:
            print("Rescuing person!")
            r.rescue_person()
            print("Taking room 5 temperature!")
            room_5_temp = r.take_temperature()
        else:
            print("Taking room 5 temperature!")
            room_5_temp = r.take_temperature()
        r.left(350)
        r.forward(350)
    else:
        print("Skipping room 5!")
    r.left(325)
    r.forward(225)
    r.left(1200)
    r.forward(700)
    r.left(800)
    r.forward(950)
    r.right(2400)
    r.backward(1425)
    print("Done!")


hallway()

plot_temp()