import psutil

def get_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return {
        "cpu": cpu_percent,
        "ram": {
            "total": round(memory.total / (1024**2)),   # MB 단위
            "used": round(memory.used / (1024**2)),
            "percent": memory.percent
        },
        "disk": {
            "total": round(disk.total / (1024**3)),     # GB 단위
            "used": round(disk.used / (1024**3)),
            "percent": disk.percent
        }
    }

