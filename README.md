# Smart Answerer

## This program gives you the best answer randomly according to the data it gets from the Database.db file. Of course, with the percentage of sensitivity and the limit that you set for it.

<hr>

### By defining the LIMITATION variable, it specifies the minimum number of responses that must be given to a message like yours to respond to it, which is set to 5 by default.

<br>

```python
LIMITATION = 5
```

<hr>

### When the SENSITIVITY variable is defined, it separates the answers whose ratio to the total answers, with a percentage greater than the value we defined for this variable, note that this variable has a percentage aspect and must be defined between the numbers 0 and 100, which It is set to 40% by default.

<br>

```python
SENSITIVITY = 40
```

<hr>

## For example, we have such data:

<table border>
    <thead>
        <tr>
            <th>message</th>
            <th>replied</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Hello</td>
            <td>Hello, How are you?</td>
        </tr>
        <tr>
            <td>Hello</td>
            <td>Hello</td>
        </tr>
        <tr>
            <td>Hello</td>
            <td>Hello</td>
        </tr>
        <tr>
            <td>Hello</td>
            <td>Hi</td>
        </tr>
        <tr>
            <td>Hello</td>
            <td>Hi</td>
        </tr>
    </tbody>
</table>

### Both Hello and Hi answers have a percentage of 40% in the answers, and they are confirmed based on the SENSITIVITY variable, and the answer Hello, How are you? which percentage ratio is 20%, it is not confirmed that the program chooses one of these two answers randomly and gives the answer:

```console
>> Hello
Hi
>> Hello
Hello
```

<br>

**Finally, you can provide more data to the program and give more answers to your message.**
