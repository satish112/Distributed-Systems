from multiprocessing import Process, Lock, Pool
import os, os.path


def file(count, l):
    if count == '1':
        try:
            l.acquire()

            if not os.path.exists('C:/Users/RELLA/Desktop/python/cc.txt'):
                with open('C:/Users/RELLA/Desktop/python/cc.txt', 'x') as f:
                    f.write(str(0))
            else:
                with open('C:/Users/RELLA/Desktop/python/cc.txt', 'r+') as f:
                    data = int(f.read())
                    f.write(str(data + 1))
        finally:
            l.release()

    if count == '2':
        try:
            l.acquire()

            if not os.path.exists('C:/Users/RELLA/Desktop/python/cc.txt'):
                with open('C:/Users/RELLA/Desktop/python/cc.txt', 'x') as f:
                    f.write(str(0))
            else:
                with open('C:/Users/RELLA/Desktop/python/cc.txt', 'r+') as f:
                    data = int(f.read())
                    f.write(str(data + 1))
        finally:
            l.release()

    if count == '1':
        try:
            l.acquire()

            if not os.path.exists('C:/Users/RELLA/Desktop/python/cc.txt'):
                with open('C:/Users/RELLA/Desktop/python/cc.txt', 'x') as f:
                    f.write(str(0))
            else:
                with open('C:/Users/RELLA/Desktop/python/cc.txt', 'r+') as f:
                    data = int(f.read())
                    f.write(str(data + 1))
        finally:
            l.release()







#
if __name__ == '__main__':


    lock = Lock()
    p1 = Process(target=file, args=('1', lock))
    p1.start()
    p1.join()

    p2 = Process(target=file, args=('2', lock))
    p2.start()
    p2.join()

    p3 = Process(target=file, args=('3', lock))
    p3.start()
    p3.join()
#   p =multiprocessing.Pool(3)
#    p.map(p1, p2, p3)