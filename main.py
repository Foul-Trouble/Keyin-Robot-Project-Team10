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

r.disconnect()
