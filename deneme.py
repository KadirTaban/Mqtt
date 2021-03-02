import multiprocessing

def spawn_process(i):
   print ('Frame is processing: %s', %i)
   return

if __name__ == '__main__':
   Process_jobs = []
   for i in range(3):
        p = multiprocessing.Process(target = spawn_process, args = (i,))
        Process_jobs.append(p)
   p.start()
   p.join()
