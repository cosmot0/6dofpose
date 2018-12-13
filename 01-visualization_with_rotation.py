# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import DDUtil
import DDUtilDraw
#dat = np.loadtxt ("pose/out_20170919_010635_555719_pose.txt")
#dat = np.loadtxt ("pose/out_20170919_010615_996641_pose.txt")

# 다음은 2018/12/05 수업시간에 측정한 장치의 pose 입니다. 본인의 파일을 열어 보세요

#Stream_181205_144136
#fn = "Stream_181205_154126.txt"
fn = "Stream_181205_152946.txt"
dat = np.loadtxt ("pose/"+fn)


print('dat.shape (before) =', dat.shape)

# 너무 촘촘해서 띄엄띄엄 그리기 위함
nJump = 1 # 필요에 따라 늘려서 해보세요
dat = DDUtil.GetSparseIDX(dat, nJump)

dat = np.array(dat)
print('dat.shape (after) =', dat.shape)

# 매 순간 회전, x/y/z 축 Column vectors
bUseIndex=False

if bUseIndex:
    rx = dat[:, 1:4]
    ry = dat[:, 5:8]
    rz = dat[:, 9:12]

    # Translation (3자유도 위치)
    x = dat[:, 12 + 1]
    y = dat[:, 13 + 1]
    z = dat[:, 14 + 1]

else:
    rx = dat[:, 0:3]
    ry = dat[:, 4:7]
    rz = dat[:, 8:11]

    x = dat[:, 12 ]
    y = dat[:, 13 ]
    z = dat[:, 14 ]
#print(rx[0], ry[0], rz[0])
print(dat[0])

print('rx.shape =', rx.shape)
print('x.shape =', x.shape)

# 그림 그리기 시작
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(x, y, z, c='r', marker='.')

#시작점을 별(*)로 표시
ax.scatter(x[0], y[0], z[0], c='r', marker='*',  s=100)

DDUtilDraw.DrawAxis(ax, x, y, z, rx, ry, rz, scale= 0.02) # axis 그리기

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_aspect('equal')
plt.title(fn)
plt.show()




