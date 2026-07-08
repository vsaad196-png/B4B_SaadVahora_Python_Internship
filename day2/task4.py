bk_prc=45

print("1.calculate tche total cost of 7 book" )
total=bk_prc*7

print(f'the cost of 7 notebook::{total}')

print("2.how many book bought in 500 rs")
bg=(500//45)
print(f"the notebook can be bought in 500 budget::{bg}")

print("3.Calculates how much money is left over after buying the maximum number of notebooks, using modulus")

mn_lf=bg%bk_prc

print(f"the money left::{mn_lf}")