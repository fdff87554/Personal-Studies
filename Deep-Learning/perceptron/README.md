# Perceptron - 感知器

## What is Perceptron? / 什麼是感知器?
* Perceptron Algorithm 是由美國研究人員 Rosenblatt 於 1957 年提出的演算法。
* Percaptron 又被稱為 人工神經元 (Artificial Neuron) 或者 單純感知器 (Simple Perceptron)，是一個訊號處理器，接受多個輸入訊號，輸出一個訊號，且輸出訊號為二元的，分別代表往下一層傳遞或是不傳遞，也就是 0 或 1。
* 下圖為接收兩個輸入訊號的 Perceptron 模型，$x_1$、$x_2$ 為輸入訊號，$y$ 為輸出訊號，$w_1$、$w_2$ 為權重 (w 是 weight 的縮寫)，當今天輸入的訊號被傳送到 Perceptron (神經元) 時，會分別乘上權重 (可以想像成這個訊號的對判斷的影響力 or 重要性)，神經元會將所有輸入訊號的加權總，並檢查此總和是否大於某個閥值 (threshold)，若大於閥值，則輸出 1，否則輸出 0。
  > ![Perceptron-with-two-inputs-and-weights]()
* Perceptron 的運作原理就只有上述而已，也因此其公式可以表示入下:
  > $y = \begin{cases} 0 & \text{if } w_1x_1 + w_2x_2 \leq \theta \\ 1 & \text{if } w_1x_1 + w_2x_2 > \theta \end{cases}$
  > 
  > 其中，$\theta$ 為閥值 (threshold)，當 $w_1x_1 + w_2x_2$ 大於 $\theta$ 時，輸出 1，否則輸出 0。
* Perceptron 的輸入訊號可以是任何數值，但輸出訊號只有 0 或 1，因此 Perceptron 可以被視為一個二元分類器 (binary classifier)。

## What can Perceptron do? / 感知器能做什麼?
* 當 Neural Network 的概念出來時，其希望達到的效果就是超越一般 Computing Logic，也就是能夠解決一般 Computing Logic 所無法解決的問題，因此換句話說，基本 Computing Logic 能夠解決的問題，Neural Network 也要能夠解決。
* Perceptron 由於是一個二元分類器，並且也是一個線性分類器 (linear classifier)，因此只能解決線性可分 (linearly separable) 的問題，也就是說，只能解決能夠用一條直線將兩個類別分開的問題，這就是 Perceptron 的局限性。
* 而在一般單純的邏輯電路中，AND、NAND、OR Gate 都是線性可分的，因此 Perceptron 也可以解決，但 XOR Gate 卻是線性不可分的，因此 Perceptron 也無法解決，這也是為什麼 Perceptron 被挑戰者認為是一個局限性很大的演算法。

## How to write a Perceptron? / 如何寫一個感知器?
* 回顧 Perceptron 的邏輯，可以發現其就是一個簡單的 if-else 判斷式，因此可以用程式碼來實作，如下:
  > ```python
  > def perceptron(x1, x2, w1, w2, theta):
  >     if x1*w1 + x2*w2 > theta:
  >         return 1
  >     else:
  >         return 0
  > ```
* 今天可以順便加上偏差 (bias) 的概念，會需要 bias 的存在的理由可以參考另外一份筆記 [Bias in Neural Network]()，程式碼調整如下:
  > ```python
  > def perceptron(x1, x2, w1, w2, b, theta):
  >     if x1*w1 + x2*w2 + b > theta:
  >         return 1
  >     else:
  >         return 0
  > ```
* 因此我們可以看看假如我們今天希望利用 Perceptron 實現 AND、NAND、OR Gate，程式碼會長怎樣:
  > ```python
  > def AND(x1, x2):
  >     w1, w2, b, theta = 0.5, 0.5, -0.7, 0.0
  >     return perceptron(x1, x2, w1, w2, theta)
  > 
  > def NAND(x1, x2):
  >     w1, w2, b, theta = -0.5, -0.5, 0.7, 0.0
  >     return perceptron(x1, x2, w1, w2, theta)
  > 
  > def OR(x1, x2):
  >     w1, w2, b, theta = 0.5, 0.5, -0.3, 0.0
  >     return perceptron(x1, x2, w1, w2, theta)
  > ```
* 首先可以觀察到幾個現象，
  1. 對於 Perceptron 想實現 AND、NAND、OR Gate，其實只需要調整權重 (weight) 與偏差 (bias) 的值，對於 perceptron() 函式本身並不需要做任何修改。
  2. 要滿足現在的 AND、NAND、OR Gate 的需求，其實有眾多種不同的權重與偏差的組合，舉例來說對於 AND Gate 而言，$(w_1, w_2, b)$ 的組合可以是 Example 中的 $(0.5, 0.5, -0.7)$ 或者可以是 $(0.5, 0.5, -0.8)$, 甚至是 $(0.5, 0.5, -0.6)$，只要能夠滿足 AND Gate 的需求即可。
* 這也就是說，對於 Perceptron 來說，權重與偏差的值是可以被調整的，而這些值的調整其實就會重新定義 Perceptron 的行為。

## Can Perceptron solve XOR Gate? / 感知器能否解決 XOR Gate?
* 由於 Perceptron 是一個 Linear Classifier，因此無法解決 XOR Gate 這個線性不可分的問題，但其實還是有辦法解決的，也就是利用多個 Perceptron 來串接組成一個 Multi-Layer Perceptron (MLP)。
* 先回到 Logic Gates，假如我們今天希望利用 AND、OR、NAND Gate 來實現 XOR Gate，其實可以利用 NAND Gate 跟 OR Gate 來實現第一層，再利用 AND Gate 來實現第二層，就可以實現 XOR Gate 了，如下圖:
  > ![XOR Gate]()
* 再回到 Perceptron，前面提過 Perceptron 可以實現 AND、NAND、OR Gate，因此我們可以利用三個不同功能的 Perceptron 來實現 XOR Gate，程式碼如下:
  > ```python
  > def XOR(x1, x2):
  >     s1 = NAND(x1, x2)
  >     s2 = OR(x1, x2)
  >     y = AND(s1, s2)
  >     return y
  > ```
  > 其中 s1 跟 s2 就是第一層的 Perceptron 輸出，而 y 就是第二層的 Perceptron 輸出。
* 到這個時候，我們才算是真正將 Neural Network 的結構正式推出，因為他總算能完成一台電腦應該要能完成的邏輯概念了。
