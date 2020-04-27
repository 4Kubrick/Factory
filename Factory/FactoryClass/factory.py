class OperationList:
    def __init__(self):
        self.__list_operation = []

    def add_operation(self, operation):
        self.__list_operation.append(operation)

    def run_operation(self, img):
        if img is not None:
            for op in self.__list_operation:
                img = op.img_operation(img)
            return img
