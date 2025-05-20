import re

class EmailAddressParser:
    def __init__(self,addresses):
        self.addresses=addresses
    
    def parse(self):
        # Extract only valid email addresses
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', self.addresses)
        
        # Remove duplicates and sort
        return sorted(set(emails))