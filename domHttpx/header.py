from domHttpx import config

def header():
    header = f'''         
     _           _  _ _   _            
  __| |___ _ __ | || | |_| |_ _ ____ __
 / _` / _ \ '  \| __ |  _|  _| '_ \ \ /
 \__,_\___/_|_|_|_||_|\__|\__| .__/_\_\\
                             |_| v{config.version}       
                             
            naufalardhani.com
'''
                                  
    print(header)