servos.P0.setAngle(0)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P0) == 1) {
        pins.servoWritePin(AnalogPin.P1, 0)
        basic.showIcon(IconNames.No)
    } else {
        basic.showIcon(IconNames.Heart)
        pins.servoWritePin(AnalogPin.P1, 90)
        for (let index = 0; index < 5; index++) {
            music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.InBackground)
            basic.pause(2000)
        }
        pins.servoWritePin(AnalogPin.P1, 0)
    }
})
