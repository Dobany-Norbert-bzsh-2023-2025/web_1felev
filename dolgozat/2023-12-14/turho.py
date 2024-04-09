# File: turho.py
# Author: Dobány Norbert Andor
# Copyright: 2023, Dobány Norbert Andor
# Group: Szoft I/1/N
# Date: 2023-12-14
# Github: https://github.com/
# Licenc: GNU GPL

print("Dobány Norbert Andor, Szoft I/1/N, 2023-12-14")

f=open("turak.txt","w", encoding="utf-8")

hosszStr=""        
while hosszStr!="vege":
    hosszStr=input("Túraútvonalak hossza (m): ")
    if hosszStr!="vege":
        f.write(f"{hosszStr}\n")
        hosszInt=int(hosszStr)
        if hosszInt>8000:
            print("Nagy túra")
        else:   
            print("Kis túra")
f.close()
