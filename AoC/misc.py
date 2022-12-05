from subprocess import check_call

def copy(text):
    cmd = "echo {}|clip".format(text)
    try:
        check_call(cmd, shell = True)
        print("Copy successful.")
    except FileNotFoundError:
        print("Copy failed.")