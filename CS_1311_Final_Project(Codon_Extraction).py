#CS 1311 Final Project: Codon Extraction
#Objective: Input RNA Sequence, Output RNA Sequence, codons, and amino acids


#Chris Cantu - Extract Codons function, translate and display function, main function
#Eric Dominguez - Generate random RNA sequence function, export json file

import random
import json

#Create new text file called results.txt
codon_file = open("results.txt" , "w+")



#Main Function. User selects a choice whether to manually input a sequence or generate a string rondomly
def main():
    
    choice = "yes"
    while(choice == "yes"):
        print("------RNA Decoder-----")
        print("1. Manual Input")
        print("2. Generate String")
        selection = int(input("Select a number from one to two: "))
        if(selection == 1):
            RNA = input("Type the the RNA using the letters A, U, G, and C: ")
            extract_codons(RNA)
        if(selection == 2):
            length = int(input("Type the length of the string: "))
            RNA = generate_string(length)
            print("RNA: ", RNA, '\n')
            codon_file.write("RNA: ")
            codon_file.write(RNA)
            codon_file.write('\n')
            extract_codons(RNA)
        
        choice = input("Would you like to try again? Type yes to continue, type no to exit: ")
        
        #If choice equals to yes, the contents in results.txt is erased
        if(choice == 'yes'):
            codon_file.seek(0)
            codon_file.truncate()
    print("results.txt and codons.json has been written into the directory")
    print("Goodbye")
    codon_file.close()
    
            
            
            
        
    
    
#Randomly generate an RNA sequence using only the letters A, C, G, and U
def generate_string(N, alphabet='ACGU'):
    return ''.join([random.choice(alphabet) for i in range(N)])
    
    
    
#Read and translate the codons in the list    
def translate_and_display(codons):
    print("-------Amino Acids--------")
    codon_file.write("-------Amino Acids--------")
    codon_file.write('\n')
    
    for i in range(0, len(codons)):
        j = 0
        Found = False
        while(Found == False):
            
            #If the first letter in codons[i] starts with A
            if(codons[i][j] == 'A'):
                if(codons[i][j+1] == 'A'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G'):
                        print(codons[i], ": Lysine")
                        codon_file.write(codons[i])
                        codon_file.write(": Lysine \n")
                        Found = True
                    elif(codons[i][j+2] == 'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Asparagine")
                        codon_file.write(codons[i])
                        codon_file.write(" Asparagine \n")
                        Found = True
                if(codons[i][j+1] == 'G'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G'):
                        print(codons[i], ": Arginine")
                        codon_file.write(codons[i])
                        codon_file.write(" Arginine \n")
                        Found = True
                    if(codons[i][j+2] == 'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Serine")
                        codon_file.write(codons[i])
                        codon_file.write(": Serine \n")
                        Found = True
                if(codons[i][j+1] == 'C'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] == 'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Threonine")
                        codon_file.write(codons[i])
                        codon_file.write(": Threonine \n")
                        Found = True
                if(codons[i][j+1] == 'U'):
                    if(codons[i][j+2] == 'G'):
                        print(codons[i], ": Methionine")
                        codon_file.write(codons[i])
                        codon_file.write(": Methionine \n")
                        Found = True
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Isoleucine")
                        codon_file.write(codons[i])
                        codon_file.write(": Isoleucine \n")
                        Found = True
            
            #If the first letter in codons[i] starts with G
            if(codons[i][j] == 'G'):
                if(codons[i][j+1] == 'A'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G'):
                        print(codons[i], ": Glutamic Acid")
                        codon_file.write(codons[i])
                        codon_file.write(": Glutamic Acid \n")
                        Found = True
                    if(codons[i][j+2] == 'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Aspartic Acid")
                        codon_file.write(codons[i])
                        codon_file.write(": Aspartic Acid \n")
                        Found = True
                if(codons[i][j+1] == 'G'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Glycine")
                        codon_file.write(codons[i])
                        codon_file.write(": Glycine \n")
                        Found = True
                if(codons[i][j+1] == 'C'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Alanine")
                        codon_file.write(codons[i])
                        codon_file.write(": Alanine \n")
                        Found = True
                if(codons[i][j+1] == 'U'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Valine")
                        codon_file.write(codons[i])
                        codon_file.write(": Valine \n")
                        Found = True
            
            #If the first letter in codons[i] starts with C
            if(codons[i][j] == 'C'):
                if(codons[i][j+1] == 'A'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G'):
                        print(codons[i], ": Glutamine")
                        codon_file.write(codons[i])
                        codon_file.write(": Glutamine \n")
                        Found = True
                    if(codons[i][j+2] == 'U' or codons[i][j+2] ==  'C'):
                        print(codons[i], ": Histidine")
                        codon_file.write(codons[i])
                        codon_file.write(": Histidine \n")
                        Found = True
                if(codons[i][j+1] == 'G'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Arginine")
                        codon_file.write(codons[i])
                        codon_file.write(": Arginine \n")
                        Found = True
                if(codons[i][j+1] == 'C'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Proline")
                        codon_file.write(codons[i])
                        codon_file.write(": Proline \n")
                        Found = True
                if(codons[i][j+1] == 'U'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Leucine")
                        codon_file.write(codons[i])
                        codon_file.write(": Leucine \n")
                        Found = True
                        
            #If the first letter in codons[i] starts with U
            if(codons[i][j] == 'U'):
                if(codons[i][j+1] == 'A'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G'):
                        print(codons[i], ": STOP")
                        codon_file.write(codons[i])
                        codon_file.write(": STOP \n")
                        Found = True
                    if(codons[i][j+2] == 'U' or codons[i][j+2] ==  'C'):
                        print(codons[i], ": Tyrosine")
                        codon_file.write(codons[i])
                        codon_file.write(": Tyrosine \n")
                        Found = True
                if(codons[i][j+1] == 'G'):
                    if(codons[i][j+2] == 'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Cysteine")
                        codon_file.write(codons[i])
                        codon_file.write(": Cysteine \n")
                        Found = True
                    if(codons[i][j+2] == 'A'):
                        print(codons[i], ": STOP")
                        codon_file.write(codons[i])
                        codon_file.write(": STOP \n")
                        Found = True
                    if(codons[i][j+2] == 'G'):
                        print(codons[i], ": Tryptophan")
                        codon_file.write(codons[i])
                        codon_file.write(": Tryptophan \n")
                        Found = True
                if(codons[i][j+1] == 'C'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Serine")
                        codon_file.write(codons[i])
                        codon_file.write(": Serine \n")
                        Found = True
                if(codons[i][j+1] == 'U'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G'):
                        print(codons[i], ": Leucine")
                        codon_file.write(codons[i])
                        codon_file.write(": Leucine \n")
                        Found = True
                    if(codons[i][j+2] == 'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Phenylalanine")
                        codon_file.write(codons[i])
                        codon_file.write(": Phenylalanine \n")
                        Found = True
                
        
        
        
        
    #Display the number of codons along with writing the number to file results.txt
    codon_file.write('\n')
    print('\n')
    length = len(codons)
    print("Number of Codons: ", length)
    codon_file.write("Number of Codons: ")
    codon_file.write(str(length))
 
       
        
            
            
            
            
            
            
            
            
            
#Take the RNA sequence and extract every codon that exists        
def extract_codons(RNA):
    
    #Initialize Values and create a list called codons
    record = False
    char_1 = char_2 = char_3 = False
    record_off_switch_1 = record_off_switch_2 = record_off_switch_3 = False
    r_1 = r_2 = False
    ch_1 = ch_2 = ch_3 = False
    skip1 = skip2 = False
    record_off_lock = record_on_lock = False
    switch = switch2 = False
    begin_recording = False
    increment = increment2 = True
    skipagain = skipagain2 = False
    codons = []
    
    #Display and write the title into text file results.txt 
    print("----Codons----")
    codon_file.write('\n')
    codon_file.write("----Codons----")
    codon_file.write('\n')
    
    #Extraction begin
    for i in range(0, len(RNA)):
        
        #No codons are recorded 
        if(record == False and begin_recording == False):
            if(switch2 == False):
                #When A is encountered, the number is assigned to start and verification for AUG begins
                if(RNA[i] == 'A'):
                    start = i
                    char_1 = True
                    record_off_lock = True
            if(switch2 == True and record_off_lock == True):
                if(record_off_switch_1 == True and increment == True and skip1 == False):
                    char_2 = True
                if(record_off_switch_1 == record_off_switch_2 == True and increment == True and skip2 == False):
                    char_3 = True
                if(record_off_switch_1 == record_off_switch_2 == record_off_switch_3==True):
                    end = i
                    codon = RNA[start:end]
                    
                    #If codon is AUG, append AUG into list, begin recording                      
                    if(codon == "AUG"):
                        print(codon)
                        codon_file.write(codon)
                        codon_file.write('\t')
                        codons.append(codon)
                        record = True
                        record_off_switch_1 = record_off_switch_2 = record_off_switch_3 = False
                        char_1 = char_2 = char_3 = False
                        record_off_lock = False
                        switch2 = False
                        skip1 = skip2 = False
                    
                    #Else, record is off
                    else:
                        record_off_switch_1 = record_off_switch_2 = record_off_switch_3 = False
                        char_1 = char_2 = char_3 = False
                        record_off_lock = False
                        switch2 = False 
                        skip1 = skip2 = False
                        
            
            
            if(record_off_lock == True and char_1 == True):
                switch2 = True
            if(char_1 == True and record == False):
                record_off_switch_1 = True
                increment = True
            if(char_1 == char_2 == True and record == False):
                record_off_switch_2 = True
                skip1 = True
            if(char_1 == char_2 == char_3 == True and record == False):
                record_off_switch_3 = True
                skip2 = True
            
        #Codons are recorded    
        if(record == True and begin_recording == True):
            if(record_on_lock == False):
                start = i-1
                ch_1 = True
                record_on_lock = True
            if(switch == True and record_on_lock == True):
                if(r_1 == True and increment2 == True and skipagain == False):
                    ch_2 = True
                if(r_1 == r_2 == True and increment == True and skipagain2 == False):
                    end = i
                    codon = RNA[start:end]
                    
                    #if codon is equal to either UGA, UAA, or UAG, append into list, but stop recording
                    if(codon == "UGA" or codon == "UAA" or codon == "UAG"):
                        codons.append(codon)
                        print(codon)
                        codon_file.write(codon)
                        codon_file.write('\t')
                        record = False
                        r_1 = r_2 = False
                        ch_1 = ch_2 = ch_3 = False
                        record_on_lock = False
                        switch = False
                        skipagain = skipagain2 = False
                     
                    #Else, continue recording    
                    else:
                        codons.append(codon)
                        print(codon)
                        codon_file.write(codon)
                        codon_file.write('\t')
                        r_1 = r_2  = False
                        ch_1 = ch_2 = ch_3 = False
                        record_on_lock = False
                        switch = False
                        skipagain = skipagain2 = False
            
           
            if(record_on_lock == True and ch_1 == True):
                switch = True
            if(ch_1 == True and record == True):
                r_1 = True
                increment2 = True
            if(ch_1 == ch_2 == True and record == True):
                r_2 = True
                skipagain = True
            if(ch_1 == ch_2 == ch_3 == True and record == True):
                skipagain2 = True
        
        #Record Switch
        if(record == True):
            begin_recording = True
        if(record == False):
            begin_recording = False     
        
        
        
        
    #Create file called codons.json, which stores and displays the contents of the list codons    
    filename = 'codons.json'
    with open(filename, 'w+') as f_obj:
        json.dump(codons, f_obj)
    print('\n')
    codon_file.write('\n')
    codon_file.write('\n')
    
    #Translate the codon list
    translate_and_display(codons)

                     
            
            
            
            
            
            
            
            
            

main()

