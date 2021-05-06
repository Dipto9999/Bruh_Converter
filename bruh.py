# Initialize string variables for 'BRUH' conversion.
bruh = 'BRUH'
min_bruh = 'BR'

name_too_short = 'Cannot BRUH-ify. Your name is too short.'
reduction_finished = 'Cannot be BRUH-ified further.'

#####################################################
########## 'BRUH' Conversion Functions ##############
#####################################################

def converter(phrase) :
    converted_phrase = ''
    bruh_ready = 0

    for character in range(len(phrase)) :
        if (phrase[character] == ' ') :
            ## Append BRUH if at least two additional letters at end of word.
            if (bruh_ready >= len(min_bruh)) :
                converted_phrase += bruh
            converted_phrase += ' '
            bruh_ready = 0     
        else :
            ## Increment counter in almost every case (other than when encountering ' ' character).
            bruh_ready += 1
            ## Reinitialize counter and append BRUH after every four letters.
            if (bruh_ready == len(bruh)) :   
                bruh_ready = 0
                converted_phrase += bruh 
            ## Append BRUH at end of phrase if at least two additional letters at end of word.     
            elif ((character == (len(phrase)-1)) and (bruh_ready >= len(min_bruh))) :
                converted_phrase += bruh

        ## The following lines have been commented out. -> Used for debugging loop in custom function.
        ## print('Phrase Character : ', phrase[character])        
        ## print('BRUH Ready : ', bruh_ready)
        ## print('BRUH Phrase : ', converted_phrase)
    
    if (converted_phrase == '') :
        converted_phrase = name_too_short

    return converted_phrase

def reducer(phrase) :
    reduced_bruh = ''
    bruh_count = 0
    bruh_index = 0
        
    for character in range(len(phrase)) :
        if (phrase[character] == ' ') :
            bruh_index = 0
        ## Reinitialize index and increment count after each BRUH is iterated through.
        elif (phrase[character] == bruh[len(bruh)-1]) :
            bruh_index = 0
            bruh_count += 1
        ## Increment index when iterating through a single BRUH.
        elif(phrase[character] == bruh[bruh_index]) :
            bruh_index += 1

        ## The following lines have been commented out. -> Used for debugging loop in custom function.
        ## print('Phrase Character : ' , phrase[character])        
        ## print('BRUH Index : ', bruh_index)
        ## print('BRUH Count : ', bruh_count)
    
    for counter in range(1, bruh_count + 1, 1) :
        ## Append BRUH after every four BRUHs.
        if (counter % len(bruh) == 0) :
            reduced_bruh += bruh
        elif (counter == bruh_count) :
            ## Append BRUH if at least two additional BRUHs at end of word.
            if (bruh_count % len(bruh) >= len(min_bruh)) :
                reduced_bruh += bruh

        ## The following lines have been commented out. -> Used for debugging loop in custom function.
        ## print('Counter : ' , counter)        
        ## print('Reduced BRUH Phrase : ', reduced_bruh)

    if (reduced_bruh == phrase or bruh_count <= 1) :
        return_message = reduction_finished 
    else : 
        return_message = reduced_bruh

    return return_message

#####################################################
#####################################################
#####################################################