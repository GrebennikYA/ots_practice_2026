import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5

    if state == "RIGHT1":
        t.forward(10)  # Перемещение

        if turn > num_turns:
            state = "STOP"
            return state, turn
        if x >= turn:
            state = "UP1"
            t.setheading(90)  # Разворот вверх
            return state, turn
        return state, turn
    if state == "UP2":

        return state, turn
    if state == "RIGHT2":
        t.forward(10)  # Перемещение

        if x >= turn:
            state = "DOWN2"
            t.setheading(270)  # Разворот вниз
            return state, turn
        return state, turn
    if state == "INIT":

        if True:
            state = "DOWN1"
            t.setheading(270)  # Разворот вниз
            return state, turn
        return state, turn
    if state == "UP1":
        t.forward(10)  # Перемещение

        if y >= turn:
            state = "RIGHT2"
            t.setheading(0)  # Разворот вправо
            return state, turn
        return state, turn
    if state == "DOWN1":
        t.forward(10)  # Перемещение

        if y <= -turn:
            state = "RIGHT1"
            t.setheading(0)  # Разворот вправо
            return state, turn
        return state, turn
    if state == "DOWN2":
        t.forward(10)  # Перемещение

        if y <= -turn:
            state = "RIGHT1"
            t.setheading(0)  # Разворот вправо
            turn = turn + 1  # Начало нового витка
            return state, turn
        return state, turn
    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if  __name__ == "__main__":
    draw()

# import turtle

# def perform_switch_case(state, t, side_steps, steps_on_side):
#     if state == "INIT":
#         state = "DOWN1"
#         t.setheading(270)
#         steps_on_side = 0
#         return state, steps_on_side

#     if state == "DOWN1":
#         t.forward(10)
#         steps_on_side += 1
#         if steps_on_side >= side_steps:
#             state = "RIGHT1"
#             t.setheading(0)
#             steps_on_side = 0
#         return state, steps_on_side

#     if state == "RIGHT1":
#         t.forward(10)
#         steps_on_side += 1
#         if steps_on_side >= side_steps:
#             state = "UP1"
#             t.setheading(90)
#             steps_on_side = 0
#         return state, steps_on_side

#     if state == "UP1":
#         t.forward(10)
#         steps_on_side += 1
#         if steps_on_side >= side_steps:
#             state = "RIGHT2"
#             t.setheading(0)
#             steps_on_side = 0
#         return state, steps_on_side

#     if state == "RIGHT2":
#         t.forward(10)
#         steps_on_side += 1
#         if steps_on_side >= side_steps:
#             state = "DOWN2"
#             t.setheading(270)
#             steps_on_side = 0
#         return state, steps_on_side

#     if state == "DOWN2":
#         t.forward(10)
#         steps_on_side += 1
#         if steps_on_side >= side_steps:
#             state = "STOP"  # или продолжить спираль, меняя side_steps
#         return state, steps_on_side

#     return state, steps_on_side


# def draw():
#     start_state = "INIT"
#     end_state = "STOP"
#     curr_state = start_state
#     t = turtle.Turtle()
#     t.speed(0)
#     side_steps = 5          # фиксированное число шагов на сторону
#     steps_on_side = 0       # счётчик шагов на текущей стороне

#     while curr_state != end_state:
#         curr_state, steps_on_side = perform_switch_case(curr_state, t, side_steps, steps_on_side)

#     turtle.done()


# if __name__ == "__main__":
#     draw()
