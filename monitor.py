import argparse
import psutil
from time import sleep

from log import logger
from bar import get_bar


def main():
    parser = argparse.ArgumentParser(description='Log System Monitor')
    parser.add_argument('--interval', help='time interval in seconds for monitoring', type=int, default=2)   
    args = parser.parse_args()
    
    while True:        
        cpu=psutil.cpu_percent()    
        logger.info(f"%CPU {cpu:6.2f}% {get_bar(cpu)} -")
        sleep(abs(args.interval))

if __name__ == '__main__':
    main()