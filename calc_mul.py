#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        # バックスラッシュを含むのでraw文字列のほうが安全
        p = re.compile(r"^[+-]?\d+$")
        if p.match(ai) and p.match(bi):
                a=float(ai)
                b=float(bi)
                # pythonは比較を連結できる わかりやすいので使った
                if 0<a<1000 and 0<b<1000:
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
