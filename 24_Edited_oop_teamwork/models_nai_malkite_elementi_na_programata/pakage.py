

class Package:
    def __init__(self,
                 package_id: int,
                 start_location:str,
                 end_location:str,
                 weight,
                 customer_id):

        self.package_id = package_id
        self.start_location = start_location
        self.end_location = end_location
        self.weight = weight
        self.customer_id = customer_id

