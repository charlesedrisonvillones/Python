'''Beatrice sells dresses and desktop organizers. She utilizes social media platforms in doing her live online selling to further promote her products. Her clients are not from her area, so she needs a courier to deliver the item/s to them.

Assuming that all dresses cost 50 pesos each and all desktop organizers cost 125 pesos each, create a program that will help Beatrice calculate the total price sold per customer (do not mind the shipping fee).

Note: Do not put any unit (pesos) in the output. See the sample test cases below.

Input Format
There are two lines of input. The first line consists of the number of dresses; the second line consists of the number of desktop organizers.

Sample Test Cases
Ex. #	Input	Output
1	10
2	750
2	3
10	1400
3	0
20	2500
Test Case 1: 10 dresses cost a total of 500 pesos while 2 desktop organizers cost a total of 250 pesos for a total of 750 pesos.

Try to figure out the next sample test cases!'''

dresses = int(input())
desktop_organizer = int(input())
total_price = dresses * 50 + desktop_organizer * 125
print(total_price)