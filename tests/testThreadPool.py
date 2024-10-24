import pytest
import time
from project.threadPool import ThreadPool


def task_func(value):
    # sample task
    time.sleep(0.5)
    return value


def test_init():
    # test for initialization
    pool = ThreadPool(3)
    assert pool.num_threads == 3
    assert pool.alive is True
    assert len(pool.threads) >= 3


def test_init_zero_num():
    # test with num_threads = 0
    with pytest.raises(ValueError):
        ThreadPool(0)


def test_enqueue():
    # test for enqueue
    pool = ThreadPool(2)
    pool.enqueue(task_func(5))
    assert len(pool.tasks) == 1


def test_enqueue_non_callable_task():
    # test for enqueue with noncallable task
    pool = ThreadPool(2)
    with pytest.raises(TypeError):
        pool.enqueue(42)


def test_dispose():
    # test for dispose
    pool = ThreadPool(2)
    pool.dispose()
    assert pool.alive is False
    for thread in pool.threads:
        assert not thread.is_alive()


def test_multiple_task_execution():
    # test to check that the task is running
    pool = ThreadPool(4)
    results = []

    for i in range(5):
        pool.enqueue(results.append(task_func(i)))

    time.sleep(1)
    assert len(results) == 5
    assert results == list(range(5))


def test_enqueue_after_dispose():
    # test with adding new tasks after the pool is completed
    pool = ThreadPool(2)
    pool.dispose()
    with pytest.raises(RuntimeError):
        pool.enqueue(lambda: None)


def test_thread_pool_n_threads():
    # test to check the number of threads
    n = 7
    pool = ThreadPool(n)
    assert len(pool.threads) >= n
    pool.dispose()
