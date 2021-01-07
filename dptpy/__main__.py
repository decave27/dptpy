import argparse
from .commands import Init, Zip, Help, New

def console():
    parser = argparse.ArgumentParser(description=f'Deplux unofficial setuptools')
    parser.add_argument("--kh", "--krhelp", help="Prints help in Korean", action="store_true")
    parser.add_argument("--i", "--init", "--setup", help='Create a Dockerfile for distribution', action="store_true")
    parser.add_argument('--z', "--zip", "--build", help='Compress the root directory where you ran the command to a hosted file for Deplux', action="store_true")
    parser.add_argument("--n", "--new", "--create", help="Create a new deplux project", action="store_true")
    parser.add_argument
    args = parser.parse_args()

    if args.i:
        Init()
    if args.z:
        Zip()
    if args.kh:
        Help(lang="kr")
    if args.n:
        New()




if __name__ == "__main__" :
    console()
    
    




    


