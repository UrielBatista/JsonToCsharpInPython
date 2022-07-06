from time import sleep
from src.convert import Convert


if __name__ == '__main__':

    try:

        convert_payload = Convert()
        payload = convert_payload.executor_convert()
        #print(payload)

        sleep(1)
        print('...Finish Search...')

    except Exception as exception:
        print(exception)

    finally:
        pass