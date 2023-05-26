# Day 1 : Python Basics with Code Implementation / Python 基礎與程式碼實作

## Data Structures: Introductions and Implementation with Python / 資料結構：介紹與 Python 實作

- 在數據處理和儲存的世界中，利用 Hash Table 或 Hashmap 來儲存資料是一個非常常見的方式，這個資料結構可以讓我們在 O(1) (最糟 O(n)) 的時間複雜度下，將資料儲存起來，並且在需要的時候可以快速的取得資料。
- Hash Table 通常使用一個 Array 來儲存資料，並且使用一個 Hash Function 來將資料轉換成 Array 的 Index，這樣就可以快速的將資料儲存起來，並且在需要的時候可以快速的取得資料。而當多個 Key 被轉換成相同的 Index 時，我們稱之為 Collision (碰撞)，而解決 Collision 的方式有很多種，例如：Chaining、Open Addressing 等等。
- Chaining (鏈結) 是一種處理 Collision 的做法，其在 Collision 發生的 Index 中，儲存一個 Linked List。

### Hash function / 雜湊函數

- Hash function 會將全域的 $U$ Keys 映射到 Hash Table $T[0 ... m-1]$ 的 Slots 中，基於 hash function，元素被儲存在 $h(k)$ 中，其中 $h: U \to {0,1,...,m-1}$，其中 $m$ 為 Hash Table 的大小，且遠小於 $|U|$ 的大小。

### Collision Resolution / 碰撞解決

- 如上所述，當兩個 key hash 被映射到相同的 slot 時，稱之為 Collision，而 Collision 的解決思路是 "避免碰撞" (聽起來很像廢話)。
- 那避免碰撞的一種想法是讓 $h$ 看起來是 Random (隨機) 的，但因為 $|U| > m$，因此必定最少會有兩個 key 有相同的 hash value，完全避免碰撞是不可能的，因此我們需要一個方法來處理碰撞。

#### Resolving Collision by Chaining / 鏈結解決碰撞

- Chaining 是一種處理 Collision 的做法，其在 Collision 發生的 Index 中，儲存一個 Linked List。
  > ![Hash table and Chaining - From [here](http://abutko.github.io/418project/)](https://raw.githubusercontent.com/fdff87554/Personal-Studies/main/Data-Science-and-Machine-Learning-Series/Images/Day-01/Hash-table-and-Chaining.png)
  
