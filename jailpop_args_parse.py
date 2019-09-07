import os, argparse

##########################
#  Get the arguments
##########################

def parse_arguments_fix():
	global args
	
	parser = argparse.ArgumentParser(description='Clean up CSV files, try to determine race')

	parser.add_argument('-i','--infile', dest='infile', default='short_names.csv',
	#                   required=True,
	                   help='Input file - should be a CSV file with arguments in first row')

	parser.add_argument('-o','--outfile', dest='outfile', type=str, default='placeholder_file',
	                   help='name of outfile')

	parser.add_argument('-d','--outdir', dest='outdir', type=str, default='output',
	                   help='Location for the output files')

	parser.add_argument("-v", "--verbose", dest='verbose', type=int, default=2,
	                    help="increase output verbose")


	args = parser.parse_args()
	if args.verbose >= 3: print("Initial args:",args)
	if args.outfile == "placeholder_file":
	  args.outfile=os.path.join(args.outdir, args.infile)
	if args.verbose >= 3: print("Reworked args:",args)
	return args
