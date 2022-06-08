from unittest.mock import Mock, call
from todolist.app import ToDoApp
from todolist.commands import QuitCommand
import pytest


# def test_todoapp_prompt():
#     input = Mock(return_value='quit')
#     output = Mock()
#     app = ToDoApp(io=(input, output))

#     app.run()

#     assert output.call_args_list[0] == call("ToDo List:\n\n\n> ")


# def test_todoapp_quit_prints_bye_and_exits():
#     input = Mock(return_value='quit')
#     output = Mock()
#     app = ToDoApp(io=(input, output))

#     app.run()

#     assert output.call_args_list[-1] == call('Bye!\n')


# def test_todoapp_loops_until_quit():
#     input = Mock(side_effect=['cmd', 'cmd', 'cmd', 'quit'])
#     output = Mock()
#     app = ToDoApp(io=(input, output))

#     app.run()

#     assert output.call_args_list[-1] == call('Bye!\n')


##############################################################

@pytest.fixture
def input_mock():
    return Mock()


@pytest.fixture
def output_mock():
    return Mock()


@pytest.fixture
def app(input_mock, output_mock):
    app = ToDoApp(io=(input_mock, output_mock))
    return app


def test_todoapp_prompt(input_mock, output_mock, app):
    input_mock.return_value = 'quit'

    app.run()

    assert output_mock.call_args_list[0] == call("TODOs:\n\n\n> ")


def test_todoapp_quit_prints_bye_and_exits(input_mock, output_mock, app):
    input_mock.return_value = 'quit'

    app.run()

    assert output_mock.call_args_list[-1] == call('Bye!\n')


def test_todoapp_loops_until_quit(input_mock, output_mock, app):
    input_mock.side_effect = ['cmd', 'cmd', 'cmd', 'quit']
    app.register_cmd("cmd", Mock())

    app.run()

    assert output_mock.call_args_list[-1] == call('Bye!\n')


def test_todoapp_loop_executes_command(input_mock, output_mock, app):
    cmd_mock = Mock()
    input_mock.side_effect = ['cmd', 'quit']
    app.register_cmd("cmd", cmd_mock)

    app.run()

    cmd_mock.execute.assert_called_once()

######################################################

# def test_command_quit_break_the_loop_of_app(app):
#     cmd = QuitCommand(app)

#     assert app._is_running == True

#     cmd.execute()

#     assert app._is_running == False