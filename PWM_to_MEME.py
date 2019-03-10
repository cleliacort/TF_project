##USAGE:python PWM_to_MEME.py [name_of_folder_contaning_PWMs]
##EXAMPLE:python PWM_to_MEME.py pwms
##NoteBene:the script is not well optimized
import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Trasform a CIS_BP format matrix into a MEME format.')
parser.add_argument('-mf','--matricesFolder',type=str, metavar='', required=True, default='.', help='The folder name where are the PWMs saved.')
parser.add_argument('-out','--outputName',type=str, metavar='', required=False, default='MEME_PWMs', help='The folder name where the PWMs in MEME format will be saved.')
args=parser.parse_args()

pwm_folder=args.matricesFolder
##make the directory for the meme output
name_meme_PWM_folder=""
if args.outputName:
    name_meme_PWM_folder=args.outputName
else:
    name_meme_PWM_folder="MEME_PWMs"
meme_command="mkdir "+name_meme_PWM_folder
os.system(meme_command)

##for each file in the directory passed as input, open read and trasfom into meme format
for file_name in os.listdir(pwm_folder):
    name_motif=file_name.split('.txt')[0]
    ##organize the output meme name
    name_meme_out=name_motif+".meme"
    path_motif_meme=os.path.join(name_meme_PWM_folder,name_meme_out)
    MEME=open(path_motif_meme,"w")
    ##compute the length of the motif (length of the matrix in the file)
    motif=open(os.path.join(pwm_folder,file_name))
    weigth = len(motif.readlines())-1

    with open(os.path.join(pwm_folder,file_name),"r") as motif:
        ##make the header and write it in the meme output file
        header="MEME version 4.4\n\nALPHABET= ACGT\n\nstrands: + -\n\nBackground letter frequencies (from uniform background):\nA 0.25000 C 0.25000 G 0.25000 T 0.25000\n\n"
        header+="MOTIF %s\n\n"%(name_motif)
        header+="letter-probability matrix: alength= 4 w=%d nsites= 20 E= 0\n"%(weigth)
        MEME.write(header)
        ##add line by line the matrix to the meme output file
        for line in motif:
            line=line.rstrip()
            comple_line=""
            if line.startswith('Pos'):
                continue #for skipping the print of empty line for the line contaning the Pos
            ##cycle over the sting to get the frequencies of each base
            for freq in range (1,5):
                if freq==4:
                    comple_line+=line.split('\t')[freq]
                    weigth+=1
                else:
                    comple_line+=line.split('\t')[freq]+"\t"
                    weigth+=1
            MEME.write(comple_line+"\n")
