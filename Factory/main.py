from Factory.FactoryClass.operation import InversImage, RotateImage, SmoothingImage
from Factory.FactoryClass.factory import OperationList
import cv2

def add_opperation(oper):
    select = True
    while select:
        print("\n1. Obrut na 90 stopni\n2. Inversja\n3. Wygładzenie\n4. Pokaz obrazek")
        choose1 = input("Podaj liczbę >> ")
        if choose1 == "1":
            oper.add_operation(RotateImage())
        elif choose1 == "2":
            oper.add_operation(InversImage())
        elif choose1 == "3":
            oper.add_operation(SmoothingImage())
        elif choose1 == "4":
            select = False
        else:
            print("\nPodany nieprawidłowy znak\n")


def main():
    img_path = ""
    oper = OperationList()
    get_path = True
    while get_path:
        img_path = input("Podaj sciezke do obrazu> ")#"nickel.jpeg"
        im_in = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if im_in is not None:
            get_path = False
        else:
            print("Sciezka do pliku jest bledna")

    do_op = True
    while do_op:
        add_opperation(oper)
        im_th = oper.run_operation(im_in)
        cv2.imshow("Result", im_th)
        cv2.waitKey(10)
        select = input("1.Zapisz\r\n0. Wyjdz\r\n >> ")
        if select == "1":
            cv2.imwrite(img_path, im_th)
        if select == "0":
            do_op = False


if '__main__' == __name__:
    main()
