import zmq
import time

context = zmq.Context()

# Socket to send messages on
sender = context.socket(zmq.PUSH)
sender.connect("tcp://192.168.69.40:5555")

sender.send_string("deltaRobot>Home>")

print("Done")

time.sleep(2)
