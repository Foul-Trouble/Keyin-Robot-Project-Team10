import robot_mac
import matplotlib as plt
r = robot_mac.RobotController()
r.connect()
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


def room_5():
    r.forward(1450)
    r.rotate_counterclockwise(90)
    r.forward(2400)
    r.rotate_counterclockwise(90)
    r.forward(900)
    r.rotate_counterclockwise(90)
    r.forward(900)
    r.rotate_clockwise(90)
    r.forward(700)
    r.rotate_counterclockwise(90)
    r.forward(900)
    r.rotate_clockwise(30)
    r.forward(575)
    if r.read_marker() == 1:
        r.rotate_clockwise(60)
        r.forward(350)
        r.rotate_counterclockwise(90)
        r.forward(250)
        global room_5_temp
        room_5_temp = r.take_temperature()
        if r.scan_for_people():
            r.rescue_person()
            r.rotate_counterclockwise(180)
            r.forward(250)
            r.rotate_clockwise(90)
            r.forward(350)
            r.rotate_counterclockwise(60)
            r.forward(575)
            r.rotate_counterclockwise(30)
            r.forward(900)
            r.rotate_clockwise(90)
            r.forward(700)
            r.rotate_counterclockwise(90)
            r.forward(900)
            r.rotate_clockwise(90)
            r.forward(900)
            r.rotate_clockwise(90)
            r.forward(2415)
            r.rotate_clockwise(90)
            r.forward(1450)
            r.rotate_clockwise(180)
        else:
            r.rotate_counterclockwise(180)
            r.forward(250)
            r.rotate_clockwise(90)
            r.forward(350)
            r.rotate_counterclockwise(60)
            r.forward(575)
            r.rotate_counterclockwise(30)
            r.forward(900)
            r.rotate_clockwise(90)
            r.forward(700)
            r.rotate_counterclockwise(90)
            r.forward(900)
            r.rotate_clockwise(90)
            r.forward(900)
            r.rotate_clockwise(90)
            r.forward(2415)
            r.rotate_clockwise(90)
            r.forward(1450)
            r.rotate_clockwise(180)
    else:
        r.rotate_counterclockwise(180)
        r.forward(575)
        r.rotate_counterclockwise(30)
        r.forward(900)
        r.rotate_clockwise(90)
        r.forward(700)
        r.rotate_counterclockwise(90)
        r.forward(900)
        r.rotate_clockwise(90)
        r.forward(900)
        r.rotate_clockwise(90)
        r.forward(2415)
        r.rotate_clockwise(90)
        r.forward(1450)
        r.rotate_clockwise(180)

        
def room1():
    r.forward(400)
    r.rotate_counterclockwise(90)
    mark = r.read_marker()
    if mark == 1:
        print(mark)
        r.forward(790)
        r.rotate_clockwise(90)
        r.forward(50)
        people_scan()
        global room_1_temp
        room_1_temp = r.take_temperature()
        r.backward(50)
        r.rotate_clockwise(90)
        r.forward(790)
        r.rotate_clockwise(90)
        r.forward(390)
        r.rotate_clockwise(180)
        r.forward(950)
        r.rotate_counterclockwise(90)
        r.forward(100)
        return
    elif mark == 2:
        r.rotate_clockwise(90)
        r.forward(500)
        r.rotate_counterclockwise(90)
        return


def room2():
    mark = r.read_marker()
    if mark == 1:
        print(mark)
        r.forward(685)
        r.rotate_clockwise(90)
        r.forward(50)
        fire_loop()
        global room_2_temp
        room_2_temp = r.take_temperature()
        r.backward(50)
        r.rotate_clockwise(90)
        r.forward(750)
        r.rotate_counterclockwise(90)
        r.forward(500)
        r.rotate_counterclockwise(90)
        r.forward(1750)
        r.rotate_counterclockwise(90)
        r.forward(100)
        r.rotate_clockwise(45)
        return
    if mark == 2:
        return


def room3():
    m = r.read_marker()
    print(m)
    if m == 1:
        r.rotate_counterclockwise(45)
        r.forward(200)
        global room_3_temp
        room_3_temp = r.take_temperature()
    else:
        return

room1()
room2()

