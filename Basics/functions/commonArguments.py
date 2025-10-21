from argParse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--output',required= True, help = 'The destination file to be supplied')
args = parser.parse_args()
print(args.output)