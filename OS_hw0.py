import multiprocessing


def producer(data_pipe, ack_pipe):
    # Generate numbers 1 through 5.
    for number in range(1, 6):
        print(f"Producer: {number}", flush=True)

        data_pipe.send(number)

        ack_pipe.recv()


def consumer(data_pipe, ack_pipe):
    for number in range(1, 6):
        number = data_pipe.recv()

        print(f"Consumer: {number}", flush=True)

        ack_pipe.send("done")


def main():

    data_pipe = multiprocessing.Pipe()

    ack_pipe = multiprocessing.Pipe()

    producer_process = multiprocessing.Process(
        target=producer,
        args=(data_pipe[1], ack_pipe[0])
    )


    consumer_process = multiprocessing.Process(
        target=consumer,
        args=(data_pipe[0], ack_pipe[1])
    )

    # Start both processes.
    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()


if __name__ == "__main__":
    main()