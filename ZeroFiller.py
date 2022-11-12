import pickle, argparse, sys

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(prog = 'ZeroFiller', description = 'Append \'0\'s to a file many times to increase the file size by the specified number of megabytes.')
    parser.add_argument('-i', help='-i INPUT_FILE', type=str)
    parser.add_argument('-s', help='-s SIZE_IN_MEGABYTES', type=str)
    args = parser.parse_args()
    
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit()
    
    f = open(args.i,"ab")
    data_size = int(args.s) * 1024 * 1024
    padding = "0" * data_size
    pickle.dump(padding, f)
    f.close()