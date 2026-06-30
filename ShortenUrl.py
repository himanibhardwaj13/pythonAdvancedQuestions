import string
import random
url_db = {}
class ShortenService:
    @staticmethod
    def shorten_code(length):
        chars = string.ascii_letters+string.digits
        while True:
            code = ''.join(random.choice(chars) for _ in range(length))
            if code not in url_db:
                return code
                
    @staticmethod
    def shorten_url(long_url, length):
        short_code = ShortenService.shorten_code(length)
    
        url_db[short_code] = long_url
    
        return ShortenService.create_url(short_code)
        
    @staticmethod
    def create_url(short_code):
        return f"http://helpme/{short_code}"
        
    @staticmethod
    def origin_url(short_code):
        return url_db[short_code]

    
print(ShortenService.shorten_url('https://www.google.com', 6))
