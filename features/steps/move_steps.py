from behave import given, then, when

from features.steps.src.commands.fuel import FuelMovement
from features.steps.src.commands.move import MoveCommand
from features.steps.src.commands.rotate import ChangeVelocityCommand


@given('Тело находится в точке ({x}, {y}) пространства')
def given_the_body_located_at_the_point(context, x, y):
    context.mock.set_position([int(x), int(y)])


@given('Тело, у которого невозможно определить положение в пространстве')
def given_the_body_which_is_unable_to_located(context):
    context.exception = None
    try:
        raise ValueError('невозможно определить положение в пространстве')
    except Exception as e:
        context.exception = e.__class__.__name__


@given('имеет скорость ({x}, {y})')
def when_the_body_has_velocity(context, x, y):
    context.mock.get_velocity.configure_mock(return_value=[int(x), int(y)])


@when('выполняется операция MoveCommand')
def when_the_body_moves(context):
    MoveCommand(context.mock).execute()


@given('невозможно установить новое положение тела в пространстве')
def it_is_impossible_to_change_position_of_the_body(context):
    context.exception = None
    try:
        raise ValueError(
            'невозможно установить новое положение тела в пространстве'
        )
    except Exception as e:
        context.exception = e.__class__.__name__


@then('новое положение тела в пространстве определяется точкой ({x}, {y})')
def then_the_body_should_be_moved_to_point(context, x, y):
    assert context.mock.get_position() == [int(x), int(y)],\
        f"current position {context.mock.get_position()}"


@when('невозможно определить мгновенную скорость')
def when_it_it_unable_to_get_velocity_value(context):
    context.exception = None
    try:
        raise ValueError('невозможно определить мгновенную скорость')
    except Exception as e:
        context.exception = e.__class__.__name__


@given('количество топлива ({x})')
def given_fuel(context, x):
    context.fuel.set(int(x))


@given('расход топлива ({x})')
def given_consumption(context, x):
    context.fuel.set_consumption(int(x))


@when('двигаемся расходуя топливо и проверяя его количество')
def when_fueled_movement(context):
    context.exception = None
    try:
        FuelMovement(context.mock, context.fuel).execute()
    except Exception as e:
        context.exception = e.__class__.__name__


@then('количество топлива ({x})')
def then_fuel(context, x):
    assert context.fuel.get() == int(x), f"fuel count: {context.fuel.get()}"


@then('операция {command} прерывается выбросом исключения {exception_type}')
def then_fuel_movement_raise_exception(context, command, exception_type):
    assert context.exception == exception_type, \
        f"Invalid exception. Got:{context.exception} - expected " + \
        exception_type


@given('направление {direction} из {directions_number}')
def given_direction_and_directions_number(context,
                                          direction,
                                          directions_number):
    context.rotable.set_direction(int(direction))
    context.rotable.set_directions_number(int(directions_number))
    assert context.rotable.get_direction() == int(direction)
    assert context.rotable.get_directions_number() == int(directions_number)


@when('выполняется операция ChangeVelocityCommand')
def when_execute_change_velocity(context):
    ChangeVelocityCommand(context.mock, context.rotable).execute()
    MoveCommand(context.mock).execute()
