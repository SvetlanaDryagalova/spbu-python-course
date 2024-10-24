import threading


class ThreadPool:
    """
        The `ThreadPool` class provides an implementation of a thread pool,
        allowing for concurrent execution of tasks using a specified number
        of worker threads.
        Parameters
            num_threads : int
                The number of threads to create in the pool.
        Attributes
            num_threads : int
                Stores the number of threads in the pool.
            tasks : list
                A list that holds the tasks to be executed.
            lock : Lock object
                A threading lock to manage concurrent access.
            condition : Condition object
                A condition variable that allows threads to wait for tasks
                to become available.
            alive : bool
                A flag that indicates if the thread pool is still active.
            threads : list
                A list that holds the thread instances created for the pool.
        Methods
            worker(self)
                Looks for tasks to execute until the thread pool is marked
                as not alive.
            enqueue(self, task)
                Adds a task to the queue for execution by the worker threads.
            dispose(self)
                Signals the thread pool to terminate and waits
                for all worker threads to finish.
        """

    def __init__(self, num_threads):
        """
        Initializes the thread pool.
        Parameters
            num_threads: int
                The number of threads to create in the pool.
        Raises
            ValueError
                If num_threads is not positive integer.
        """
        if not (num_threads > 0 and isinstance(num_threads, int)):
            raise ValueError('Number of threads must be positive integer.')

        self.num_threads = num_threads
        self.tasks = []
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.alive = True
        self.threads = []

        for i in range(num_threads):
            thread = threading.Thread(target=self.worker)
            thread.start()
            self.threads.append(thread)

    def worker(self) -> None:
        """
            Looks for tasks to execute until
            the thread pool is marked as not alive.
        """
        while self.alive:
            with self.condition:
                while not self.tasks and self.alive:
                    self.condition.wait()

                if not self.alive:
                    break

                task = self.tasks.pop(0)

            print(f"Thread {threading.current_thread().name} is executing "
                  f"a task.")
            task()

    def enqueue(self, task):
        """
            Adds a task to the queue for execution by the worker threads.
            Parameters
                task : A callable to be executed by a worker thread.
            Raises
                TypeError
                    If the argument is not a callable object.
                RuntimeError
                    If the thread pool has already been terminated.
        """
        if not callable(task):
            raise TypeError("The argument must be a callable object.")

        if not self.alive:
            raise RuntimeError("Cannot add new task to terminated "
                               "thread pool.")

        with self.condition:
            self.tasks.append(task)
            self.condition.notify()

    def dispose(self):
        """
            Signals the thread pool to terminate and waits
            for all worker threads to finish.
        """
        with self.lock:
            self.alive = False
            self.condition.notify_all()
        for thread in self.threads:
            thread.join()
