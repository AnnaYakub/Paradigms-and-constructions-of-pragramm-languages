import sys
import math

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    if check_roots(coef_str):
        coef = float(coef_str)
        return coef
    else:
        return get_coef(index, prompt)
        
def check_roots(coef):
    try:
        coef = float(coef)
        return True
    except:
        print("Вы неверно ввели каэффицент!")
        return False

def get_roots(a, b, c):
    
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        if (root)>0.0:
            root1 = math.sqrt(-b / (2.0*a))
            root1 = -math.sqrt(-b / (2.0*a))
            result.append(root1,root2)
        elif root==0:
            result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        if ((-b - sqD) / (2.0*a))>0:
            root1 = math.sqrt((-b + sqD) / (2.0*a))
            root2 = -math.sqrt((-b + sqD) / (2.0*a))
            root3 = math.sqrt((-b - sqD) / (2.0*a))
            root4 = -math.sqrt((-b - sqD) / (2.0*a))
            result.append(root1)
            result.append(root2)
            result.append(root3)
            result.append(root4)
        elif ((-b - sqD) / (2.0*a))==0:
            root1 = math.sqrt((-b + sqD) / (2.0*a))
            root2 = -math.sqrt((-b + sqD) / (2.0*a))
            root3 = math.sqrt((-b - sqD) / (2.0*a))
            result.append(root1)
            result.append(root2)
            result.append(root3)
        elif ((-b + sqD) / (2.0*a))>0:
            root1 = math.sqrt((-b + sqD) / (2.0*a))
            root2 = -math.sqrt((-b + sqD) / (2.0*a))
            result.append(root1)
            result.append(root2)
        elif ((-b + sqD) / (2.0*a))==0:
            root1 = math.sqrt((-b + sqD) / (2.0*a))
            result.append(root1)
    return result

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    
    roots = get_roots(a,b,c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {},{},{} и {}'.format(roots[0], roots[1],roots[2],roots[3]))
if __name__ == "__main__":
    main()
