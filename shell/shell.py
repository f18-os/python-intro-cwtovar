#! /usr/bin/env python3

import os, sys, time, re

def getPostion(command, searchee):
    for idx, operand in enumerate(command):
        if operand == searchee:
            return idx
while(True):
    position=0
    directive=input("Shell of the Tovar $>").split()
    print(directive)
    if '>' in directive:
        position=int(getPostion(directive, '>'))

        pid = os.getpid()               # get and remember pid
        print('position', position)

        os.write(1, ("About to fork (pid=%d)\n" % pid).encode())

        rc = os.fork()

        if rc < 0:
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)

        elif rc == 0:                   # child
            os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" % 
                         (os.getpid(), pid)).encode())
            del directive[position]
            args=directive
            print('args', args)

            os.close(1)                 # redirect child's stdout
            sys.stdout = open(args[position], "w")
            fd = sys.stdout.fileno() # os.open("p4-output.txt", os.O_CREAT)
            os.set_inheritable(fd, True)
            os.write(2, ("Child: opened fd=%d for writing\n" % fd).encode())

            for dir in re.split(":", os.environ['PATH']): # try each directory in path
                program = "%s/%s" % (dir, args[0])
                try:
                    os.execve(program, args, os.environ) # try to exec program 
                except FileNotFoundError:             # ...expected
                    pass                              # ...fail quietly 

            os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
            sys.exit(1)                 # terminate with error

        else:                           # parent (forked ok)
            os.write(1, ("Parent: My pid=%d.  Child's pid=%d\n" % 
                         (pid, rc)).encode())
            childPidCode = os.wait()
            os.write(1, ("Parent: Child %d terminated with exit code %d\n" % 
                         childPidCode).encode())
    if '<' in directive:
        position=getPostion(directive, '<')

        pid = os.getpid()               # get and remember pid

        os.write(1, ("About to fork (pid=%d)\n" % pid).encode())''

        rc = os.fork()

        if rc < 0:
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)

        elif rc == 0:                   # child
            os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" % 
                         (os.getpid(), pid)).encode())
            args = directive.remove(position)

            os.close(0)                 # redirect child's stdout
            sys.stdout = open(args[position], "r")
            fd = sys.stdout.fileno() # os.open("p4-output.txt", os.O_CREAT)
            os.set_inheritable(fd, True)
            os.write(2, ("Child: opened fd=%d for writing\n" % fd).encode())

            for dir in re.split(":", os.environ['PATH']): # try each directory in path
                program = "%s/%s" % (dir, args[0])
                try:
                    os.execve(program, args, os.environ) # try to exec program 
                except FileNotFoundError:             # ...expected
                    pass                              # ...fail quietly 

            os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
            sys.exit(1)                 # terminate with error

        else:                           # parent (forked ok)
            os.write(1, ("Parent: My pid=%d.  Child's pid=%d\n" % 
                         (pid, rc)).encode())
            childPidCode = os.wait()
            os.write(1, ("Parent: Child %d terminated with exit code %d\n" % 
                         childPidCode).encode())+

    else:     
        pid = os.getpid()               # get and remember pid

        os.write(1, ("About to fork (pid=%d)\n" % pid).encode())

        rc = os.fork()

        if rc < 0:
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)

        elif rc == 0:                   # child
            os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" % 
                         (os.getpid(), pid)).encode())
            args = directive

            for dir in re.split(":", os.environ['PATH']): # try each directory in path
                program = "%s/%s" % (dir, args[0])
                try:
                    os.execve(program, args, os.environ) # try to exec program
                except FileNotFoundError:             # ...expected
                    pass                              # ...fail quietly 

            os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
            sys.exit(1)                 # terminate with error

        else:                           # parent (forked ok)
            os.write(1, ("Parent: My pid=%d.  Child's pid=%d\n" % 
                         (pid, rc)).encode())
            childPidCode = os.wait()
            os.write(1, ("Parent: Child %d terminated with exit code %d\n" % 
                         childPidCode).encode())
