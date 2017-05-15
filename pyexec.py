script = input('Python script file: ')
with open(script) as f:
    cmd = f.read()
    print(cmd)
    print('***************')
    exec(cmd)
