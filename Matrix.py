# Mat1=[[1,2,3,4],
#      [5,6,7,8]]
# Mat2=[[1,2,3,4],
#      [5,6,7,8]]
# Mat3 = [[0 for _ in range(len(Mat1[0]))] for _ in range(len(Mat1))]
# if len(Mat1) == len(Mat2) and len(Mat1[0]) == len(Mat2[0]):
#     for i in range(len(Mat1)):
#         for j in range(len(Mat1[0])):
#             Mat3[i][j] = Mat1[i][j] + Mat2[i][j]
# print(Mat3)
Mat1=[[1,2,3],
     [4,5,6],
     [7,8,9]]
Mat2=[[1,2,3,5],
     [4,5,6,5],
     [7,8,9,5]]
Mat3=[[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]
for i in range(len(Mat1)):
    for j in range(len(Mat2[0])):
        for k in range(len(Mat2)):
            Mat3[i][j]+=Mat1[i][k]*Mat3[k][j]
print(Mat3)
