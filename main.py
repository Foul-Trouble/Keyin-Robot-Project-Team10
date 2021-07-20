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
r.rotate

r.disconnect()


def fire_loop():
    Fire = True
    while Fire:
        if r.scan_for_fire():
            r.extinguish_fire()
        else:
            Fire = False





