import psutil


def monitor_cpu(procesos, stop_event, info_procesos):
    while not stop_event.is_set():
        for idx, p in enumerate(procesos, 1):
            try:
                ps = psutil.Process(p.pid)
                nuc = ps.cpu_num()
                info_procesos[idx] = {"pid": p.pid, "nucleo": nuc}
            except psutil.NoSuchProcess:
                pass
        stop_event.wait(timeout=2)
