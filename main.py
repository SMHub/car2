def on_button_pressed_a():
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

Tinybit.RGB_Car_Big(Tinybit.enColor.WHITE)

def on_every_interval():
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, Tinybit.Ultrasonic_Car())
loops.every_interval(500, on_every_interval)
