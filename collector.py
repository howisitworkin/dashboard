import psutil

def get_cpu_usage():
	return psutil.cpu_percent(interval=1)

def get_memory_usage():
	mem = psutil.virtual_memory()
	return {
		'total': mem.total,
		'available': mem.available,
		'used': mem.used,
		'percent': mem.percent
	}

def get_disk_usage(path='/'):
	disk = psutil.disk_usage(path)
	return {
		'total': disk.total,
		'used': disk.used,
		'free': disk.free,
		'percent': disk.percent
	}

def collect_metrics():
	return {
		'cpu': get_cpu_usage(),
		'memory': get_memory_usage(),
		'disk': get_disk_usage()

	}

if __name__ == "__main__":
	import json
	print(json.dumps(collect_metrics(), indent=2))
