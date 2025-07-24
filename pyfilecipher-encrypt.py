# =================Other Configuration================  
# Usages : 
usage = "usage: %prog [options]" 
# Version 
Version = "%prog 0.0.1" 
# ==================================================== 

# Import Modules 
import optparse, sys, os 
from toolkit import processor as ps 

def main(): 
    parser = optparse.OptionParser(usage=usage, version=Version)
    parser.add_option('-i', '--input', type='string', dest='inputfile',
                      help="File Input Path For Encryption", default=None)
    parser.add_option('-o', '--output', type='string', dest='outputfile',
                      help="File Output Path For Saving Encrypted Cipher", default=".")
    parser.add_option('-p', '--password', type='string', dest='password',
                      help="Provide Password For Encrypting File", default=None)

    (options, args) = parser.parse_args()

    # Input Conditions Checkings 
    if not options.inputfile or not os.path.isfile(options.inputfile): 
        print("[Error] Please Specify a Valid Input File Path") 
        sys.exit(0) 

    if not options.outputfile or not os.path.isdir(options.outputfile): 
        print("[Error] Please Specify a Valid Output Path (existing folder)") 
        sys.exit(0) 

    if not options.password: 
        print("[Error] No Password Provided") 
        sys.exit(0) 

    inputfile = options.inputfile
    filename_wo_ext = os.path.splitext(os.path.basename(inputfile))[0]
    outputfile = os.path.join(options.outputfile, filename_wo_ext + '.ssb')
    password = options.password 
    work = "E"  # E for Encrypt

    ps.FileCipher(inputfile, outputfile, password, work) 
    return 

if __name__ == '__main__': 
    main()
