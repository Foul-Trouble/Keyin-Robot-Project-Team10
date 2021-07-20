import robot_mac
r = robot_mac.RobotController()
r.connect()

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
        r.forward(2400)
        r.rotate_clockwise(90)
        r.forward(1450)
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
        r.forward(2400)
        r.rotate_clockwise(90)
        r.forward(1450)
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
    r.forward(2400)
    r.rotate_clockwise(90)
    r.forward(1450)




r.disconnect()


def fire_loop():
    Fire = True
    while Fire:
        if r.scan_for_fire():
            r.extinguish_fire()
        else:
            Fire = False





