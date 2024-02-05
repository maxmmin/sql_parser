from subprocess import CompletedProcess


def check_out_exec_err(exec_res: CompletedProcess):
    if exec_res.returncode is not 0:
        raise Exception("An exception occurred during database creating:"
                        f"\n\nExit code: {exec_res.returncode}"
                        f"\n\nError output: {exec_res.stderr}")
