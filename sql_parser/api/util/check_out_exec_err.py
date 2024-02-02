from docker.models.containers import ExecResult


def check_out_exec_err(exec_res: ExecResult):
    if exec_res.exit_code is not 0:
        raise Exception("An exception occurred during database creating:"
                        f"\n\nExit code: {exec_res.exit_code}"
                        f"\n\nOutput: {exec_res.output}")
