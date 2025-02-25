# Behavioral Patterns (行為模式)

行為模式涉及對象之間的通信，它們如何相互交互以及它們之間的職責分配。

## Included Patterns

### 1. Observer (觀察者)
- 定義對象之間的一對多依賴關係，當一個對象狀態改變時，所有依賴於它的對象都會得到通知
- 參考 `observer.py`

### 2. Strategy (策略)
- 定義一系列算法，將每個算法都封裝起來，並且使它們之間可以互換
- 參考 `strategy.py`

### 3. Command (命令)
- 將請求封裝為一個對象，從而使你可以用不同的請求對客戶進行參數化
- 參考 `command.py`

### 4. State (狀態)
- 允許一個對象在其內部狀態改變時改變它的行為
- 參考 `state.py`

### 5. Template Method (模板方法)
- 定義一個操作中的算法骨架，而將某些步驟延遲到子類中實現
- 參考 `template_method.py`

### 6. Chain of Responsibility (責任鏈)
- 將請求的發送者和接收者解耦，使多個對象都有機會處理這個請求
- 參考 `chain_of_responsibility.py`

### 7. Iterator (迭代器)
- 提供一種方法順序訪問一個聚合對象中的各個元素，而不需要暴露其內部表示
- 參考 `iterator.py`

### 8. Mediator (中介者)
- 定義一個中介對象來封裝一系列對象之間的交互
- 參考 `mediator.py`

### 9. Memento (備忘錄)
- 在不破壞封裝性的前提下，捕獲一個對象的內部狀態，並在該對象之外保存這個狀態
- 參考 `memento.py`

### 10. Visitor (訪問者)
- 在不改變各元素類別的前提下定義作用於這些元素的新操作
- 參考 `visitor.py`

### 11. Interpreter (解釋器)
- 定義一個語言的文法，並且建立一個解釋器來解釋該語言中的句子
- 參考 `interpreter.py`

### 12. Null Object (空對象)
- 通過一個空對象來替代NULL對象實例的檢查
- 參考 `null_object.py`