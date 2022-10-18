import time
from pyinstrument import Profiler

profiler = Profiler()
profiler.start()

sleep_time = 0.1

def start():
    time.sleep(sleep_time)
    do_sleep1()
    do_sleep2()

def do_sleep1():
    time.sleep(sleep_time)

def do_sleep2():
    do_sleep1()
    time.sleep(sleep_time)

start()

profiler.stop()
profiler.print()
profiler.open_in_browser()