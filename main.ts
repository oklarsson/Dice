basic.forever(function on_forever() {
    input.onGesture(Gesture.Shake, function on_gesture_shake() {
        let result = randint(1, 6)
        console.log(result)
    })
})
