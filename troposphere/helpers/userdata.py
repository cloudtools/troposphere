import os
from troposphere import Base64, Join

# helper function to import and format existing file as userdata
# filepath must be an absolute filepath

def from_file(filepath):
    """Imports userdata from a file.
    
    This function ignore blank lines within the file.
    Special characters are automatically escaped.

    Args:
        filepath (string): The absolute path to the file containing the userdata to be imported.

    Returns:
        Base64 object: The Base64 object being passed a Join object with strings.
        If file not found, an empty string list is used.

    """
    
    data = []
    
    try:
        f = open(filepath, "r")
        try:
            for line in f:
                if line.strip():
                    data.append(line)
        except:
            print "Error: Could not parse userdata file - No userdata imported."
            data = []
        
    except IOError:
        print "Error: Userdata file does not appear to exist. - No userdata imported."

    finally:
        return Base64(Join(",", data))