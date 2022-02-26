# Uniquely Building Parse Trees
 Building a parse tree from a non-parenthesized mathematical expression, using Python.


# ![Uniquely Building Parse Trees](DemoImages/AlgorithmIntroDemo.png)

## **How it works** 🤔

First, [download](https://www.python.org/downloads/) and install **Python**. Version `3.7` or higher is recommended.


Let's now run the main file, `uniqueParseTrees.py`, no requirements needed, etc.

```bash
python uniqueParseTrees.py
```

That's all you need to know to start!

---

You are now asked to input some non-parenthesized expression as the following

```bash
5 + 2 * 3 + 10 / 2
```

when given such input, the algorithm (implemented in the `buildingUniqueParseTrees` in the `uniqueParseTrees.py` file) is all about splitting the expression into properly ordered sub-expressions.

Then, it starts building its own tree, using the first sub-expression, and so on, looping through the remaining sub-expressions.

### Notice that

The precedence of operators needs to be defined **manually** of course as follows:
```python
operators = {"-": 0, "+": 0, "*": 1, "/": 1}
```

<br>

Here's a quick visual example of what is really happening:

<br>

## starting off by taking the first sub-expression, implementing it manually
<img src="DemoImages/1.png" />

## given an operator, we create a temporary tree with the operator as its root value, inserting a right child pointed at by `current2`

<img src="DemoImages/2.png" />

## now lets check the precedence
`The operator * has higher precedence than +`

<img src="DemoImages/3.0.png" />

## In such case, we do the following steps:

<img src="DemoImages/3.1.png" />
<img src="DemoImages/3.2.png" />
<img src="DemoImages/3.3.png" />

## we are now left off at this **state**: 

<img src="DemoImages/4.png" />

## given an operand, we will store it in the position pointed at by `current2`

<img src="DemoImages/4.1.png" />

## here's the current **state** of our tree:
<img src="DemoImages/4.2.png" />

## given another operator, we create a temporary tree with the operator as its root value, inserting a right child pointed at by `current2`, once again.

<img src="DemoImages/5.png" />

## well, this time the operator stored at `t` or the `+` operator, has lower precedence. In such case, we do the following steps: 

<img src="DemoImages/6.png" />


<img src="DemoImages/6.1.png" />
<img src="DemoImages/6.2.png" />
<img src="DemoImages/6.3.png" />
<img src="DemoImages/6.4.png" />
<img src="DemoImages/6.5.png" />

## we are now left off at this **state**, once again

<img src="DemoImages/7.png" />

## now, given an operand, store it in the position pointed at by `current2`

<img src="DemoImages/7.1.png" />

<br>
<br>

<h2 align="center" style="font-weight: bold;">and so on...</h2>

<br>
<br>

## here's the final state of our uniquely built parse tree:

<img src="DemoImages/8.png" />

## and that's about it.

<br>
<br>

## ⚒️ **Built with**

<br>


- [Python](https://www.w3schools.com/python/python_reference.asp) - Python is a popular programming language used in many fields.


<br>


## [License](https://github.com/mostafa-aboelnaga/Terminalio/blob/main/LICENSE)

MIT © [Mostafa Aboelnaga](https://github.com/mostafa-aboelnaga/)
