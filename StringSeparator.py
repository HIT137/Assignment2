class StringSeparator:
    def __init__(self, s):
        self.s = s
        self.numbers = ''
        self.letters = ''
    
    def separate(self):
        for char in self.s:
            if char.isdigit():
                self.numbers += char
            elif char.isalpha():
                self.letters += char
    
    def convert_even_numbers_to_ascii(self):
        even_numbers_ascii = [str(ord(char)) for char in self.numbers if int(char) % 2 == 0]
        self.even_numbers_str = ''.join(even_numbers_ascii)
    
    def convert_uppercase_letters_to_ascii(self):
        upper_case_ascii = [str(ord(char)) for char in self.letters if char.isupper()]
        self.upper_case_str = ''.join(upper_case_ascii)
    
    def process(self):
        self.separate()
        self.convert_even_numbers_to_ascii()
        self.convert_uppercase_letters_to_ascii()
    
    def display_results(self):
        print("Even Numbers:", self.even_numbers_str)
        print("ASCII CODE of Even Numbers:", ', '.join(self.even_numbers_str))
        print("Upper-case Letters:", self.upper_case_str)
        print("ASCII CODE Decimal values of Upper-case Letters:", ', '.join(self.upper_case_str))


s = '56aAww1984sktr235270aYmn145ss785fsq31D0'
separator = StringSeparator(s)
separator.process()
separator.display_results()
