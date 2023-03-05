#!/usr/bin/python3

import sys
import os
import subprocess
import threading
from itertools import combinations

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None
        self.result = None
        
    def target(self):      
               #print('Thread started: {} {} '.format(self.cmd, self.result))
               self.process = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, shell=False)
               stdoutdata, stderrdata = self.process.communicate()            
               #print('Thread finished {}'.format( stdoutdata ))
               self.result = stdoutdata
        
    def run(self, timeout):                  
               thread = threading.Thread(target = self.target )
               thread.start()
               result = thread.join(timeout)
               if thread.is_alive():
                     #print('Terminating process')
                     self.process.terminate()
                     thread.join()    
                     return None        
               return self.result

def read_optimizations_def_file():
        with open('compiler_flags.defs', 'r') as f_object:
          word_lst = f_object.read().split()
          return word_lst
          
def run_subprocess(cmd, optimization ):
               command = Command(cmd);             
               output = command.run( timeout=3)                     
               return output;
               



def main():
    sys.stdout.write("RESULT: OPTIMIZATION, INCREMENTS\n")
    optimizations = read_optimizations_def_file()
    for n in range(len(optimizations) + 1):        
               for optimization_tuple in combinations(optimizations, n):
                   optimization_str = ' ';
                   for optimization in optimization_tuple:
                       optimization_str = optimization_str + ' ' + optimization
                   print("-----------------------------------")
                   os.system( "killall -9 program_run" );
                   print( "optimization = %s" % optimization_str )
                   gcc_command = "g++ {}  -o program_run optimization_check.cpp -lpthread".format( optimization_str );
                   print( "running gcc: %s" % gcc_command );
                   retval = os.system( gcc_command );
                   print( "compille result {}".format(retval))
                   if retval == 0:
                       output = run_subprocess("./program_run", optimization_str )
                       if output:
                           sys.stdout.write("RESULT: {},{}\n".format( optimization_str, str(output) ) )
                       else:
                           sys.stdout.write("RESULT: {}, timeout\n".format(optimization_str) )


if __name__ == "__main__" :
    main()



