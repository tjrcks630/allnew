import numpy as np

#array 변수 안에 리스트로 해당 값 넣음
array = np.array([1.57, 2.48, 3.93, 4.33])
print('\narray print')
print(array)

#ceil 확인
print('\nnp.ceil() function')
result = np.ceil(array)
print(result)

#floor 확인
print('\nnp.floor() function')
result = np.floor(array)
print(result)

#round 확인
print('\nnp.round() function')
result = np.round(array)
print(result)

#decimal 확인
print('\n1 decimal place round')
result = np.round(array, 1)
print(result)

#sqrt 확인
print('\nsqrt() function')
result = np.sqrt(array)
print(result)

#arr 변수에 arange로 10의 값 할당
arr = np.arange(10)
print(arr)
print()

#exp 확인
print('\nexp() function')
result = np.exp(arr)
print(result)

#x 와 y 변수에 해당 리스트 할당
x = [5, 4]
y = [6, 3]

#maximum 확인
print('\nnp.maximum(x, y)')
result = np.maximum(x, y)
print(result)

print('-' * 30)

#array1 과 array2 변수에 해당 값 할당
array1 = np.array([-1.1, 2.2, 3.3, 4.4])
print('\narray')
print(array1)

array2 = np.array([1.1, 2.2, 3.3, 4.4])
print('\narray2')
print(array2)

#abs 확인
print('\nabs() function')
result = np.abs(array1)
print(result)

#sum 확인
print('\nsum() function')
result = np.sum(array1)
print(result)

#compare 확인
print('\ncompare')
result = np.equal(array1, array2)
print(result)

#equal 확인
print('\nnp.sum() and np.equal')
print('\nTure is 1, False is - countung.')
result = np.sum(np.equal(array1, array2))
print(result)

#mean 확인
print('\naverage')
result = np.mean(array2)
print(result)

arrX = np.array([[1,2], [3,4]], dtype = np.float64)
arrY = np.array([[5,6], [7,8]], dtype = np.float64)

print('\nadd of element by element')
print(arrX + arrY)
print(np.add(arrX, arrY))

print('\nsub of element by element')
print(arrX - arrY)
print(np.subtract(arrX, arrY))

print('\nmul of element by element')
print(arrX * arrY)
print(np.multiply(arrX, arrY))

print('\ndiv of element by element')
print(arrX / arrY)
print(np.divide(arrX, arrY))

print('\nsqrt of element by element')
print(np.sqrt(arrX))