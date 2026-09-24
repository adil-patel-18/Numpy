# 🟢 NumPy Practice Questions — Day 1

#Q1. NumPy import karke `[10, 20, 30, 40, 50]` ka array banao.
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr)

#Q2. `[5, 10, 15, 20, 25]` ka NumPy array banao aur print karo.
arr=np.array([5,10,15,20,25])
print(arr)

#Q3. Ek array `[1, 2, 3, 4, 5]` banao aur uska `ndim` print karo.
arr=np.array([1, 2, 3, 4, 5])
print(arr.ndim)

#Q4. Array `[10, 20, 30, 40]` ka `shape` print karo.
arr=np.array([10,20,30,40])
arr.shape

#Q5.Array `[10, 20, 30, 40, 50, 60]` ka `size` print karo.
arr=np.array([10,20,30,40,50,60])
arr.size

#Q6. Array `[10, 20, 30]` ka `dtype` print karo.
arr=np.array([10,20,30])
arr.dtype

#Q7. Ek NumPy array banao:
#[100, 200, 300, 400]
#Aur `ndim`, `shape`, `size`, `dtype` sab print karo.
arr=np.array([100, 200, 300, 400])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

#Q8.2D NumPy array banao:
#[[1, 2, 3],
#[4, 5, 6]]
#Aur iska `ndim` aur `shape` print karo.
arr=np.array([[1, 2, 3],[4, 5, 6]])
print(arr.ndim)
print(arr.shape)

#Q9. 2D array banao:
#[[10, 20],
 #[30, 40],
 #[50, 60]]
#Iska `shape` aur `size` find karo.
arr=np.array([[10, 20],[30, 40],[50, 60]])
print(arr.shape)
print(arr.size)

#Q10. NumPy array banao:
#[2, 4, 6, 8, 10]
#Aur uska first element aur last element print karo.
arr=np.array([2, 4, 6, 8, 10])
print(arr[0])
print(arr[-1])


# 🔥 Challenge

#Q11.** User se 5 numbers input lekar NumPy array banao aur print karo.
import numpy as np
it=1
list=[]
for i in range(1,6):
    num=int(input("Enter number :"))
    list.append(num)
arr=np.array(list)
print(arr)

#Q12. Array: [10, 20, 30, 40, 50]
# mein se `30` print karo.
arr=np.array([10,20,30,40,50])
print(arr[2])

#Q13.Array: [10, 20, 30, 40, 50]
#mein se first 3 elements print karo.
print(arr[0:3])

#Q14. Array: [10, 20, 30, 40, 50]
#mein se last 2 elements print karo.
print(arr[-2:])

#Q15. 1D aur 2D NumPy array dono banao aur unka `ndim` compare karke print karo.
arr1D=np.array([1,2,3,4,5])
arr2D=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr1D.ndim)
print(arr2D.ndim)

# Ab hum NumPy ke next important topic par jaate hain: **array operations and `arange()`**.

# 🟢 NumPy Day 1 — Q16 to Q20
#Q16. Array `[10, 20, 30, 40, 50]` banao aur uska **size** `print()` karo.
arr=np.array([10,20,30,40,50])
print(arr.size)

#Q17.** Array `[10, 20, 30, 40, 50]` banao aur uska **sum** `np.sum()` se find karo.
arr=np.array([10,20,30,40,50])
print(np.sum(arr))

#Q18. Array `[10, 20, 30, 40, 50]` ke har element mein **5 add** karo aur result print karo.
arr=np.array([10,20,30,40,50])
arr=arr+5
print(arr)

#Q19.** Array `[10, 20, 30, 40, 50]` ke har element ko **2 se multiply** karo.
arr=np.array([10,20,30,40,50])
arr=arr*2
print(arr)

#Q20. `np.arange()` use karke **1 se 10** tak numbers ka NumPy array banao.
arr=np.arange(1,11)
print(arr)

# Ab hum **NumPy calculations + conditions** practice karenge.

#Q21.** Array `[10, 20, 30, 40, 50]` ka **mean (average)** `np.mean()` se find karo.
arr=np.array([10,20,30,40,50])
print(np.mean(arr))

#Q22.** Array `[10, 20, 30, 40, 50]` ka **maximum value** `np.max()` se find karo.
arr=np.array([10,20,30,40,50])
print(np.max(arr))

#Q23.** Array `[10, 20, 30, 40, 50]` ka **minimum value** `np.min()` se find karo.
arr=np.array([10,20,30,40,50])
print(np.min(arr))

#Q24.** Array `[10, 20, 30, 40, 50]` ke har element ko **10 se divide** karo.
arr=np.array([10,20,30,40,50])
arr=arr/10
print(arr)

#Q25.** Array `[10, 15, 20, 25, 30]` mein se sirf **20 se greater values** print karo.

arr=np.array([10,15,20,25,30])
print(arr[arr > 20])

# Boolean/conditional indexing

#Q26. Array [10, 20, 30, 40, 50] mein se even numbers print karo.
arr=np.array([10,20,30,40,50])
print(arr[arr%2==0])

#Q27. Array [10, 15, 20, 25, 30] mein se odd numbers print karo.
arr=np.array([10,15,20,25,30])
print(arr[arr%2!=0])

#Q28. np.arange() use karke 2 se 20 tak even numbers ka array banao.
arr=np.arange(2,21,2)
print(arr)

#Q29. np.arange() use karke 5 se 50 tak numbers, step 5 ke saath banao.
arr=np.arange(5,51,5)
print(arr)

#Q30. Array [10, 20, 30, 40, 50] mein 30 se greater ya equal values print karo.
arr=np.array([10,20,30,40,50])
print(arr[[arr>=30]])


#Q31.** Array `[10, 20, 30, 40, 50]` mein se **30 se less** values print karo.
arr=np.array([10,20,30,40,50])
print(arr[[arr < 30]])

#Q32. Array `[10, 20, 30, 40, 50]` mein se **20 aur 40 ke beech ki values** print karo.
arr=np.array([10,20,30,40,50])
print(arr[[(arr >20) & (arr < 40)]])

#Q33. `np.zeros()` use karke **5 zeros** ka array banao.
arr=np.zeros(5)
print(arr)

#Q34. `np.ones()` use karke **5 ones** ka array banao.
arr=np.ones(5)
print(arr)

#Q35.** `np.arange()` use karke **10 se 100 tak**, step `10` ka array banao.
arr=np.arange(10,101,10)
print(arr)

#Q36. Ye 2D array banao:
#[[10, 20, 30],
#[40, 50, 60]]
#aur iska shape print karo.
arr=np.array([[10,20,30],[40,50,60]])
print(arr.shape)

#Q37. Same array mein se 50 print karo.
print(arr[1,1])

#Q38. Same array ki first row print karo.
print(arr[0])

#Q39. Same array ki second row print karo.
print(arr[1])   

#Q40. Same array mein se last column print karo.
print(arr[:,2])