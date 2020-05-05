import time

for h in range(0, 24):
    for m in range(0, 60):
        for s in range(0, 60):
            for ds in range(0, 10):
                print(h, "H", m, "M", s, "S", ds, "ds")
                time.sleep(0.10)  #éste metedo salta cada segundo, por eso 0.10
