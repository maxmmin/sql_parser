from subprocess import CompletedProcess


def check_out_exec_err(exec_res: CompletedProcess, command: str):
    if exec_res.returncode != 0:
        raise Exception("An exception occurred during execution"
                        f"\nCommand: {command}"
                        f"\nExit code: {exec_res.returncode}"
                        f"\nError output: {exec_res.stderr}")
