import robot
r = robot.RobotController()
r.connect()

r.forward(1400)
r.rotate_counterclockwise(45)
r.forward(50)
r.rotate_counterclockwise(45)
r.forward(1000)
