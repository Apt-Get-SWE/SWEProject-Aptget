from datetime import date

class User:
    def __init__(self, fname=None, lname=None, phone=None, address=None):
        if fname is None:
            raise ValueError('ValueError: First name not specified')
        if lname is None:
            raise ValueError('ValueError: Last name not specified')
        if phone is None:
            raise ValueError('ValueError: Phone number not specified')
        if address is None:
            raise ValueError('ValueError: Address not specified')

        self.fname = fname.strip().lower()
        self.lname = lname.strip().lower()
        self.phone = phone
        self.posts = {}

        """
            address format: building,city,state,zip
                i.e. 370 Jay Street,Brooklyn,NY,11201
        """
        address = address.lower().split()
        [self.building, self.city, self.state, self.zip] = [x.strip() for x in address]

class Post:
    def __init__(self, title=None, details='', condition=None, price=None):
        if title is None:
            raise ValueError('ValueError: Title not set')

        if price is None:
            raise ValueError('ValueError: Price not set')
        elif type(price) != int:
            raise ValueError('ValueError: Invalid price')

        if condition is None:
            raise ValueError('ValueError: Condition not specified')

        self.title = title
        self.details = details
        self.condition = condition
        self.list_date = date.today()
        self.price=price
        self.sold=False

    



    