import time

def countdown(num_of_secs):
    num_of_secs = int(num_of_secs)
    while num_of_secs != 0:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='\n')
        time.sleep(1)
        num_of_secs -= 1
        
    print('BUMMMMMMM.')

inp = input('Digite o tempo desejado para ativar a bomba: ')
countdown(inp)
