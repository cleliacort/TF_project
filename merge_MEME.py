import sys
import os
import argparse


parser = argparse.ArgumentParser(description='Merge multiple MEME files into a unique file.')
parser.add_argument('-mf','--memeFolder',type=str, metavar='', required=True, default='.', help='The folder name where are the PWMs saved.')
parser.add_argument('-out','--outputName',type=str, metavar='', required=False, default='unique_MEMEs.meme', help='The folder name where the PWMs in MEME format will be saved.')
parser.add_argument('-list','--idsMotifList',type=str, metavar='', required=True, default='.', help='The folder name where are the PWMs saved.')
args=parser.parse_args()

meme_folder=args.memeFolder


#if args.outputName:
name_meme_merge_file=args.outputName
list_motif=open(args.idsMotifList)

uniq_MEME=open(name_meme_merge_file,"w")
header="MEME version 4.4\n\nALPHABET= ACGT\n\nstrands: + -\n\nBackground letter frequencies (from uniform background):\nA 0.25000 C 0.25000 G 0.25000 T 0.25000\n"
#header+="MOTIF %s\n\n"%(name_motif)
#header+="letter-probability matrix: alength= 4 w=%d nsites= 20 E= 0\n"%(weigth)
uniq_MEME.write(header)


for motif in list_motif:
    motif_file=motif.rstrip()+".meme"
    MEME=open(os.path.join(meme_folder,file_name),"r")
    for line in MEME:
        if 'MOTIF' in line:
            uniq_MEME.write("\n"+line+"\n")
        elif 'letter-probability' in line:
            uniq_MEME.write(line)
        elif '\t'in line:
            uniq_MEME.write(line)
        #    print line
