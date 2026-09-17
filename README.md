# OS_Nicholas_Weah

Q1: Why can’t two ordinary processes simply communicate by reading and writing normal variables in each other’s address spaces?
A1:The Processes are purposefully kept away from each other through the virtual memory, so one process cannot access variables in another process’s address space. Instead, processes need something for inter-process communication like a pipe, to exchange information back and forth.

Q2: A pipe has a read end and a write end. What direction does information flow through a pipe?
A2: A pipe is a mechanism that is unidirectional and relies on in-order communication. Data that is  written to the “write end” of the pipe can be read from the “read end” of it.

Q3:What happens when a process tries to read from an empty pipe? How can this behavior be useful for synchronization?
A3:Reading from an empty pipe means the process will wait until the data becomes available instead of continuing it immediately. This is useful for synchronization because one process can wait for another process to send information before continuing, making it easy to order the processes.

Q4:Why is it good practice for each process to close pipe ends that it does not use?
A4: After  the processes are created, each process will have file descriptors for both ends of the pipe (even if it only needs one). Closing the unused ends of the pipe will prevent any problems such as pipes staying open when they really should be closed.

Q5:Suppose the Producer sends the numbers 1, 2, 3, 4, 5 through one pipe and the Consumer reads them. Does this alone guarantee the following printed output order?
A5: No. A pipe guarantees that the data is delivered in order, but it does not guarantee the order the two processes print their messages. \

Design Explanation
For this program I used two separate OS processes like we were told to do. I used a Producer process and a Consumer process. It is set up so that the Producer generates the numbers 1 through 5 and sends each number to the Consumer using a pipe. A second pipe is used for synchronization. After the Consumer receives and prints a number, it sends an acknowledgment back to the Producer. The Producer waits for this acknowledgment then continues to the next number. For this program I used Python's multiprocessing library (using ai tools to help find and implement the correct one)  to create the two processes and multiprocessing.Pipe() for communication between them. After both processes finish, the main process waits for them using join().

