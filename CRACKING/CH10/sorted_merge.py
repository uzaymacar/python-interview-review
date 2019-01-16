def sorted_merge(arrA, arrB):
    # trying to sort them from the beginning (small elements) would require us to
    # shif the whole array, so you should think about going in the reverse order
    # if one way doesn't work or seems too much, always think about the reverse way!
    
    indexBuffer = len(arrA) - 1
    indexB = len(arrB) - 1
    # always use information from the question: A has large enough buffer at the end to hold B
    indexA = len(arrA) - len(arrB) - 1
  
    while indexB >= 0:
        if indexA > 0 and arrA[indexA] > arrB[indexB]:
            arrA[indexBuffer] = arrA[indexA]
            indexA -= 1
        else:
            arrA[indexBuffer] = arrB[indexB]
            indexB -= 1
        indexBuffer -= 1
    
    return arrA
            
     
print(sorted_merge([3, 6, 9, 12, 15, 21, 0, 0, 0, 0, 0], [4, 8, 12, 16, 18]))
# THE REASON WHY WE HAVE ALL THE 0'S COMES DIRECTLY FROM THE QUESTION!
# READ CAREFULLY!