import heapq
import random
import time
import types
from threading import Thread

from enum import Enum, auto


def random_delay():
    return random.random() * 5


def random_countdown():
    return random.randrange(5)


@types.coroutine
def sleep(delay):
    yield Op.WAIT, delay


async def launch_rocket(delay, countdown):
    await sleep(delay)
    for i in reversed(range(countdown)):
        print(f'{i + 1} ...')
        await sleep(1)
    print('Rocket launched!')


def rockets():
    N = 10_000
    return [
        (random_delay(), random_countdown())
        for _ in range(N)
    ]


def run_threads(rockets):
    threads = [
        Thread(target=launch_rocket, args=(delay, count))
        for delay, count in rockets
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


class State(Enum):
    WAITING = auto()
    COUNTING = auto()
    LAUNCHING = auto()


class Op(Enum):
    # Operation
    WAIT = auto()
    STOP = auto()


class Launch:
    def __init__(self, delay, countdown):
        self._state = State.WAITING
        self._delay = delay
        self._countdown = countdown

    def step(self):
        if self._state is State.WAITING:
            self._state = State.COUNTING
            return Op.WAIT, self._delay
        if self._state is State.COUNTING:
            if self._countdown == 0:
                self._state = State.LAUNCHING
            else:
                print(f'{self._countdown}...')
                self._countdown -= 1
                return Op.WAIT, 1
        if self._state is State.LAUNCHING:
            print('Rocket launched!')
            return Op.STOP, None

        assert False, self._state


def now():
    return time.time()


def run_fsm(rockets):
    start = now()
    work = [(start, i, Launch(d, c)) for i, (d, c) in enumerate(rockets)]

    while work:
        step_at, id, launch = heapq.heappop(work)
        wait = step_at - now()
        if wait > 0:
            time.sleep(wait)

        op, arg = launch.step()
        if op is Op.WAIT:
            step_at = now() + arg
            heapq.heappush(work, (step_at, id, launch))
        else:
            assert op is Op.STOP


if __name__ == '__main__':
    # run_fsm(rockets())
    launch_rocket(2, 3)
