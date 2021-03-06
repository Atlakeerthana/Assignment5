# -*- coding: utf-8 -*-
"""Assignment5(2)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uk0gY0FjS0e6BB-mHrL8aMC7BKft8aN3
"""

# -*- coding: utf-8 -*-
"""ChallengeProblem3_3.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1xGGcaT6lmL94Yu5YMgCzown-uWdscJKQ
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20, 20, 100)

y = 1*x**2 + 4*x + 5

plt.plot(x,y,label='y=$x^2$+4x+5')
plt.grid()


plt.plot(-2,1, 'o')
plt.text(2,1,'c')

#show plot
plt.ylim([-1,10])
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend()

plt.show()