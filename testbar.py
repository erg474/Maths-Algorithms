from progress.bar import Bar
import time

bar = Bar('Processing', max=20)
for i in range(20):
    i2= i*1000
    time.sleep(0.1)
    bar.next()
bar.finish()
