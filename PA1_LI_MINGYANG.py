#Name: Mingyang Li
#Original Creation Date: 12/10/2017
#Last Modification Date: 12/11/2017
#Brief Description: This is a program for final project activity #1.

# Define a main function that will finish activity #1 when called.
def main():
    # Input the old patch text.
    infile1 = open('old.txt', 'r')
    oldText = infile1.read()
    infile1.close()
    # Change all the letters in the old patch text into lower case.
    oldText = oldText.lower()
    oldText = oldText.rstrip()

    # Call the deletePunct() and deleteNoise() functions
    # to delete all the punctuations and noise words
    # to the old patch text.
    oldText = deletePunct(oldText)
    oldText = deleteNoise(oldText)

    # Convert oldText to string in order to standardize the text file.
    oldText = ' '.join(oldText)

    # Call the compConceptOld() and stemOld() functions
    # to perform the compounding concept and stemming tasks
    # to the old patch text.
    oldText = compConceptOld(oldText)
    oldText = stemOld(oldText)

    # Print the standardized old patch text to the end user.
    oldText = oldText.split(' ')
    print('The standardized old patch text is:')
    print(oldText)

    # Input the new patch text.
    infile2 = open('new.txt', 'r')
    newText = infile2.read()
    infile2.close()
    # Change all the letters in the new patch text into lower case.
    newText = newText.lower()
    newText = newText.rstrip()

    # Call the deletePunct() and deleteNoise() functions
    # to delete all the punctuations and noise words
    # to the new patch text.
    newText = deletePunct(newText)
    newText = deleteNoise(newText)

    # Convert oldText to string in order to standardize the text file.
    newText = ' '.join(newText)

    # Call the compConceptOld() and stemOld() functions
    # to perform the compounding concept and stemming tasks
    # to the old patch text.
    newText = compConceptNew(newText)
    newText = stemNew(newText)

    # Print the standardized new patch text to the end user.
    newText = newText.split(' ')
    print('The standardized new patch text is:')
    print(newText)

# Define a function which deletes all the punctuations and '\n' in the text.
def deletePunct(file):
    punctuation = [',', ';', '.', '?', '(', ')']
    for punct in punctuation:
        if punct in file:
            file = file.replace(punct, '')

    for string in file:
        if string == '\n':
            file = file.replace(string, ' ')
    return file

# Define a function which deletes all the noise words.
# The noise words are from an external .txt file.
def deleteNoise(file):
    file = file.split(' ')
    infile = open('noise_words.txt', 'r')
    noise = infile.read()
    infile.close()
    noise = noise.split('\n')

    # Delete all the noise words in oldText.
    for word1 in noise:
        for word2 in file:
            if word2 == word1:
                file.remove(word2)
    return file

# Compound concepts in the old patch text.
def compConceptOld(file):
    file = file.replace('bulletin title', 'bulletin_title')
    file = file.replace('executive summary', 'executive_summary')
    file = file.replace('cumulative security update', 'cumulative_security_update')
    file = file.replace('security update', 'security_update')
    file = file.replace('internet explorer', 'internet_explorer')
    file = file.replace('remote code execution', 'remote_code_execution')
    file = file.replace('user rights', 'user_rights')
    file = file.replace('current user', 'current_user')
    file = file.replace('administrative user rights', 'administrative_user_rights')
    file = file.replace('affected system', 'affected_system')
    file = file.replace('full user rights', 'full_user_rights')
    file = file.replace('microsoft edge', 'microsoft_edge')
    file = file.replace('specially crafted', 'specilly_crafted')
    file = file.replace('scripting engine', 'scripting_engine')
    file = file.replace('microsoft windows', 'microsoft_windows')
    file = file.replace('windows print spooler components','windows_print_spooler_components')
    file = file.replace('man-in-the-middle', 'man_in_the_middle')
    file = file.replace('mitm', 'man_in_the_middle')
    file = file.replace('print server', 'print_server')
    file = file.replace('microsoft office', 'microsoft_office')
    file = file.replace('arbitrary code', 'arbitrary_code')
    file = file.replace('windows secure kernel mode', 'windows_secure_kernel_mode')
    file = file.replace('information disclosure', 'information_disclosure')
    file = file.replace('windows kernel-mode drivers', 'windows_kernel_mode_drivers')
    file = file.replace('net framework', '.net_framework')
    file = file.replace('microsoft net framework', 'microsoft_.net_framework')
    file = file.replace('xml file', 'xml_file')
    file = file.replace('web-based application', 'web_based_application')
    file = file.replace('windows kernel', 'windows_kernel')
    file = file.replace('adobe flash player','adobe_flash_player')
    file = file.replace('windows 81','windows_8.1')
    file = file.replace('windows server 2012','windows_server_2012')
    file = file.replace('windows rt 81','windows_rt_8.1')
    file = file.replace('windows_server_2012 r2','windows_server_2012_r2')
    file = file.replace('windows 10','windows_10')
    return file

# Stem the old patch text.
def stemOld(file):
    file = file.replace('resolves','resolve')
    file = file.replace('vulnerabilities','vulnerability')
    file = file.replace('views','view')
    file = file.replace('using','use')
    file = file.replace('successfully','success')
    file = file.replace('exploited','exploit')
    file = file.replace('logged','log')
    file = file.replace('programs','program')
    file = file.replace('accounts','account')
    file = file.replace('configured','configure')
    file = file.replace('fewer','few')
    file = file.replace('less','little')
    file = file.replace('impacted','impact')
    file = file.replace('users','user')
    file = file.replace('visits','visit')
    file = file.replace('opens','open')
    file = file.replace('handles', 'handle')
    file = file.replace('objects', 'object')
    file = file.replace('logs', 'log')
    file = file.replace('runs', 'run')
    file = file.replace('uploads', 'upload')
    file = file.replace('fails', 'fail')
    file = file.replace('features', 'feature')
    file = file.replace('installed', 'install')
    file = file.replace('supported', 'support')
    file = file.replace('editions', 'edition')
    file = file.replace('customers', 'customer')
    return file

# Compound concepts in the new patch text.
def compConceptNew(file):
    file = file.replace('security update', 'security_update')
    file = file.replace('security boot', 'security_boot')
    file = file.replace('microsoft windows', 'microsoft_windows')
    file = file.replace('affected policy', 'affected_policy')
    file = file.replace('administrative privileges', 'administrative_privileges')
    return file

# Stem the new patch text.
def stemNew(file):
    file = file.replace('resolves', 'resolve')
    file = file.replace('features', 'feature')
    file = file.replace('bypassed', 'bypass')
    file = file.replace('installs', 'install')
    return file

main()
