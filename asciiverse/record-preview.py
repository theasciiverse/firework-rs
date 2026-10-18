#!/usr/bin/env python3
"""Records asciiverse/firework.cast, the catalog preview, at 100x30: the
endless random show the way av starts it (`firework`, no arguments) for a
while, then a key, which quits it. Needs asciinema 3.
Usage: record-preview.py <firework binary> <out.cast> [seconds]"""
import fcntl, os, pty, select, shutil, struct, sys, tempfile, termios, time

binary, out = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
seconds = float(sys.argv[3]) if len(sys.argv) > 3 else 25.0
home = tempfile.mkdtemp()
shutil.copy(binary, os.path.join(home, "firework"))
env = dict(os.environ, HOME=home, PATH=home + ":" + os.environ["PATH"],
           TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8")
pid, fd = pty.fork()
if pid == 0:
    os.chdir(home)  # nothing in the recording names a local path
    fcntl.ioctl(0, termios.TIOCSWINSZ, struct.pack("HHHH", 30, 100, 0, 0))
    os.execvpe("asciinema", ["asciinema", "rec", "--overwrite", "-q",
        "--window-size", "100x30", "--title", "Fireworks",
        "--capture-env", "TERM,COLORTERM,LANG", "-c", "firework", out], env)
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 30, 100, 0, 0))

end = time.time() + seconds
while time.time() < end:
    if select.select([fd], [], [], 0.05)[0]:
        try:
            os.read(fd, 1 << 16)
        except OSError:
            break
os.write(fd, b"q")
for _ in range(50):
    if os.waitpid(pid, os.WNOHANG)[0]:
        break
    try:
        os.read(fd, 1 << 16)
    except OSError:
        pass
    time.sleep(0.1)
else:
    os.kill(pid, 15)
shutil.rmtree(home, ignore_errors=True)
