from .script import Script
import keyboard


def run():
    script = Script()
    print('按 ESC 键退出')
    keyboard.wait('esc')
    print('退出')


if __name__ == "__main__":
    run()
