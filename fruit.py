class Fruit:
    count = 0

    @classmethod
    def sum_count(cls):
        cls.count += 1
        return cls.count

    def __init__(self, name: object, color: object, size: object = 'big') -> object:
        """

        :rtype: object
        """
        count = self.sum_count()
        self.name = name
        self.color = color
        self.size = size
