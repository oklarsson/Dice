def on_forever():

    def on_gesture_shake():
        result = randint(1,6)
        print(result)
    input.on_gesture(Gesture.SHAKE, on_gesture_shake)
basic.forever(on_forever)
