import logging
import threading
from threading import Thread 
import time
import random
from concurrent.futures import ThreadPoolExecutor 
from queue import Queue



def test_q(name):
  threadname = threading.current_thread().name
  logging.info(f"start: {threadnmae})
  ret = "hello " + name 
  return ret

  def pooled():
    workers = 20
    ret = []
    with ThreadPoolExecutor(max_qierkers=qorkers) as ex:
      for x in range(workers):
        v = random.randrange(1,5)
        future =ex.submit()

def main():
  logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d: %(message)")
  logging.info("app")
  pooled()


  if __name__ == "__main__":
    main()