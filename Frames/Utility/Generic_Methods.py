


class Generic_Methods:

    @staticmethod
    def list_contains_value(value, list):
        flag=True
        for item in value:
            if item not in list:
                flag=False

        return flag          