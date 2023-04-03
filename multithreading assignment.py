#!/usr/bin/env python
# coding: utf-8

#  Ques 1)  what is multithreading in python? hy is it used? Name the module used to handle threads in python

# Multithreading in Python is a technique where a program is divided into multiple threads of execution that can run concurrently. Each thread is a separate flow of control that can perform a specific task, and the threads share the same memory space, allowing them to communicate and coordinate with each other.
# 
# Multithreading is used in Python to perform multiple tasks simultaneously and make programs more efficient by utilizing the available hardware resources. It is especially useful in applications that involve I/O operations or other tasks that are blocking, as it allows the program to continue executing other tasks while waiting for the blocked task to complete.
# 
# In Python, the threading module is used to handle threads. This module provides a simple and easy-to-use interface for creating and managing threads, with support for features such as thread synchronization, thread-safe data structures, and thread communication. The threading module is part of the standard Python library, so it is available on all platforms where Python is supported.

#  Ques 2))) why threading module used? write the use of the following functions
# activeCount() currentThread() enumerate()

# The threading module in Python is used to create and manage threads in a program. There are several reasons why you might want to use threading in your Python program:
# 
# Concurrency: Threading allows multiple parts of a program to run concurrently, which can improve the performance and efficiency of the program. By running multiple threads at the same time, the program can utilize the available hardware resources more effectively.
# 
# Asynchronous I/O: Threading can be used to perform asynchronous I/O operations, where the program can continue executing other tasks while waiting for I/O operations to complete. This can be useful in applications that involve network communication, file I/O, or other types of I/O that are blocking.
# 
# Parallelism: Threading can be used to perform tasks in parallel, where multiple threads can work on the same task simultaneously. This can be useful in applications that involve heavy computation, as it can reduce the time required to complete the task.
# 
# Synchronization: Threading provides mechanisms for synchronizing access to shared resources, such as data structures or files, to avoid conflicts and ensure thread safety.
# 
# activeCount(): The activeCount() function is used to get the number of thread objects that are currently active in the program. This can be useful for monitoring the status of threads and ensuring that all threads have completed before exiting the program.
# 
# currentThread(): The currentThread() function is used to get a reference to the current thread object that is executing the function. This can be useful for identifying the current thread, and for passing the thread object to other functions for manipulation.
# 
# enumerate(): The enumerate() function is used to get a list of all thread objects that are currently active in the program. This can be useful for iterating over all active threads and performing operations on them, such as waiting for them to complete or checking their status.

# Ques 3)Explain the following functions
# run() start() join() isAlive()
# 
# run(): The run() method is the entry point for the thread. When a thread is started, its run() method is called. This method can be overridden to define the thread's behavior.
# 
# start(): The start() method is used to start the execution of a thread. When the start() method is called, the thread's run() method is executed in a separate thread of execution.
# 
# join(): The join() method is used to wait for the thread to complete its execution. When the join() method is called, the program waits until the thread completes before continuing execution.
# 
# isAlive(): The isAlive() method is used to check whether the thread is currently executing. The method returns True if the thread is currently executing, and False otherwise.

# ques 4))write a python program to create two threads. Thread one must print the list of squares and thread
# two must print the list of cubes

# In[3]:


import threading

def print_squares():
    for i in range(1, 11):
        print(f"Square of {i} = {i**2}")

def print_cubes():
    for i in range(1, 11):
        print(f"Cube of {i} = {i**3}")

t1 = threading.Thread(target=print_squares)
t2 = threading.Thread(target=print_cubes)

t1.start()
t2.start()


t1.join()
t2.join()


#   Ques 5)>> State advantages and disadvantages of multithreading

# Advantages of Multithreading:

# Improved performance: Multithreading allows a program to perform multiple tasks simultaneously, which can lead to better performance and faster execution times. This is especially useful in applications that involve I/O or other tasks that are blocking.
# 
# 

# Resource sharing: Multithreading allows threads to share resources such as memory and CPU time, which can lead to more efficient resource utilization.
# 
# Asynchronous execution: Multithreading can be used to perform asynchronous I/O operations, where the program can continue executing other tasks while waiting for I/O operations to complete. This can improve the responsiveness of the program.
# 
# Parallel processing: Multithreading can be used to perform tasks in parallel, where multiple threads can work on the same task simultaneously. This can reduce the time required to complete the task.
# 
# Disadvantages of Multithreading:
# 
# Complexity: Multithreading adds complexity to a program, making it more difficult to design, develop, and debug. It can be challenging to ensure thread safety and avoid race conditions and deadlocks.
# 
# Overhead: Multithreading introduces overhead in terms of memory and CPU time, as each thread requires its own stack and context switching between threads requires additional processing time.
# 
# Synchronization issues: Multithreading introduces synchronization issues, as threads may access shared resources simultaneously, leading to conflicts and data corruption.
# 
# Debugging challenges: Debugging multithreaded programs can be challenging, as the behavior of the program can be non-deterministic and difficult to reproduce.

# Explain deadlocks and race conditions.
# Deadlocks occur when two or more threads are waiting for each other to release resources that they need in order to proceed. Deadlocks can occur when a thread holds a resource and then tries to acquire another resource that is held by another thread, which is also waiting for the first thread to release the resource it holds. This can result in a situation where both threads are waiting for each other to release the resources they need, and neither can proceed. Deadlocks can be difficult to detect and resolve, as they can be intermittent and dependent on timing and scheduling.
# 
# Race conditions occur when two or more threads access a shared resource simultaneously and the behavior of the program depends on the order in which the threads execute. Race conditions can occur when a shared resource is not properly synchronized, allowing multiple threads to access it simultaneously. This can lead to unexpected and unpredictable behavior, as the behavior of the program depends on the timing and scheduling of the threads. Race conditions can be difficult to detect and reproduce, as they can be dependent on timing and other factors.

# In[ ]:




