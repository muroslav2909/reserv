import multiprocessing
bind = "0.0.0.0:8001"
workers = multiprocessing.cpu_count() * 2 + 1