from VersaLog import *
import time
import random

log = VersaLog(enum="detailed", show_tag=True, tag="BATCH")

def process_line(line_number: int):
    time.sleep(0.1)
    if random.random() < 0.05:
        log.warning(f"Line {line_number} took longer than expected")


def process_file(file_index: int, total_files: int):
    log.step(f"Processing file_{file_index}.txt", file_index, total_files)

    with log.timer(f"file_{file_index}.txt"):
        total_lines = 20
        for i in range(1, total_lines + 1):
            process_line(i)
            log.progress(
                title=f"file_{file_index}.txt",
                current=i,
                total=total_lines
            )


def main():
    total_files = 5

    log.info("Batch Start")

    with log.timer("Total Batch"):
        for i in range(1, total_files + 1):
            process_file(i, total_files)
            log.progress("Overall Progress", i, total_files)

    log.info("Batch Finished")


if __name__ == "__main__":
    main()
